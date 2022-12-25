from accounts import sendmail
from .models import User,AuthTokens
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from Eemail.models import Message
from django.conf import settings








class LoginView(APIView):
    auth_data=''
    def SaveAthToken(self,auth_data,user):
        auth_table=AuthTokens.objects.filter(user_id=user.id).first()
        auth=auth_data.get('access')
        if auth_table is None:
            authtoken=AuthTokens()
            authtoken.token=auth
            authtoken.user_id=user
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
        user= User.objects.filter(email=email).first()
        if not user:
            return Response({"status": "success", "data": "user not found"}, status=status.HTTP_200_OK)
        if(check_password(password,user.password)):
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                if(self.SaveAthToken(auth_data,user)):
                    return Response({'msg': 'Login Success','user':{"email":user.email,"firstname":user.firstname,"lastname":user.lastname,"id":user.id}}, status=status.HTTP_200_OK,headers={
                        'token':auth_data['access']
            })
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }    

class SignupClass(APIView):

    def post(self,request):
        request.data['password']=make_password(request.data.get('password'))
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
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
            'token':str(token.token)
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



