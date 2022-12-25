
from Eemail.models import Message,Useremail
from Eemail.graphapi.typs import UserType,MessageType
import graphene
from graphql_jwt.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


class CreateMessageMutation(graphene.Mutation):
    class Arguments:
       recipient=graphene.String(required=True)
       subject=graphene.String(required=True)
       body=graphene.String(required=True)
    compose=graphene.Field(MessageType)
   #
   #  @login_required
    def mutate(self,info,recipient,subject,body,**kwargs):
        sender=info.context.user
        try:
            recipient=Useremail.objects.get(email=recipient)
        except:
            raise Exception("EMAIL WAS NOT FOUND IN DATABASE")
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[recipient.email]
        send_mail(subject=subject,message=body,from_email=email_from,recipient_list=recipient_list,fail_silently=False)

        compose=Message.objects.create(sender=sender,recipient=recipient,subject=subject,body=body)
        return CreateMessageMutation(compose=compose) 
        
