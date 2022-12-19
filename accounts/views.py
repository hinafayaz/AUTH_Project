from accounts import sendmail
from .models import User,AuthTokens
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password


class LoginView(APIView):
    auth_data=''
    def SaveAthToken(self,auth_data,user12):
        auth_table=AuthTokens.objects.filter(user_id=user12.id).first()
        auth=auth_data.get('access')
        if auth_table is None:
            authtoken=AuthTokens()
            authtoken.token=auth
            authtoken.user_id=user12
            save=authtoken.save()
            return True
        auth_table.token=auth
        auth_table.isExpired=False
        auth_table.save()
        return True
        
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data.get('email')
        password = request.data.get('password')
        user12= User.objects.filter(email=email).first()
        if not user12:
            return Response({"status": "success", "data": "user not found"}, status=status.HTTP_200_OK)
        if(check_password(password,user12.password)):
            if user12 is not None:
                login(request, user12)
                auth_data = get_tokens_for_user(request.user)
                if(self.SaveAthToken(auth_data,user12)):
                    return Response({'msg': 'Login Success','user':{"email":user12.email,"firstname":user12.firstname,"lastname":user12.lastname,"id":user12.id}}, status=status.HTTP_200_OK,headers={
            'Cache-control': 'no-store, max-age=0',
            'token':auth_data['access'],
            'X-Frame-Options': 'DENY'})
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }    
    
    
class TestCaseForLogin(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)


class SignupClass(APIView):

    def post(self,request):
        request.data['password']=make_password(request.data.get('password'))
        slz=UserSerializer(data=request.data)
        if slz.is_valid():
            slz.save()
            return Response(slz.data,status=status.HTTP_201_CREATED)
        return Response("2 emails cant be same",status=status.HTTP_406_NOT_ACCEPTABLE)

class ForgotPassword(APIView):
    def post(self,request):
        mail=request.data.get('email')
        user=User.objects.filter(email=mail).first()
        token=AuthTokens.objects.filter(user_id=user.id).first()
        sendmail.send_mail(html='hello',to_emails=[mail],from_email='akibbaba9@gmail.com',user_id=user.id,token=token)
        return Response("Email Sended!",status=status.HTTP_206_PARTIAL_CONTENT)

    def get(self,request,id,token):
        token=AuthTokens.objects.filter(user_id=id,token=token).first()
        if token is None:
            return Response("not found",status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"id":str(token.user_id_id)},status=status.HTTP_201_CREATED,headers={
            'Cache-control': 'no-store, max-age=0',
            'token':str(token.token),
            'X-Frame-Options': 'DENY'
        })
        
class NewPassword(APIView):

    def post(self,request,id):
        tok=request.headers.get('Token')
        Id=id
        new=AuthTokens.objects.filter(token=tok,user_id=Id).first()
        if new is None:
            return Response("does not exist",status=status.HTTP_401_UNAUTHORIZED)
        
        red=User.objects.filter(id=id).first()
        red.password=make_password(request.data.get('password'))
        red.save()
        return Response("password successfully changed",status=status.HTTP_202_ACCEPTED)
