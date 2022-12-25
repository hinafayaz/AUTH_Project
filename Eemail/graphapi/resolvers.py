import graphene
from django.core.exceptions import ValidationError
from smtplib import SMTPDataError
from django.core.mail import send_mail
from django.conf import settings
from graphene_django import DjangoObjectType
from Eemail.models import Useremail,Message
from Eemail.graphapi.typs import MessageType,UserType 

def resolve_all_emails(self,info,**kwargs):
    return Message.objects.all()

def resolve_Welcome(self,info,**kwargs):
    return "WELCOME TO EMAILSYSTEM"
 
def  resolve_sendmail(self,info,**kwargs):
    
    subject="GREETINGS"
    to_email="magrayhinafayazzzz@gmail.com"
    body="CH CHUI MUBARAK YOOR TAM WATNAS"
    try:
      result=send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[to_email],fail_silently=False)
    except SMTPDataError:
     #raise Exception ("email not sent")
     raise ValidationError({"internet": ValidationError("You dont have internet connection.",code=123,) } )

    return "message send successfully"  










            
            
            

