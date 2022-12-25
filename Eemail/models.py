from tkinter import CASCADE
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Useremail(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=45)
    created_on=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=45)
    lastname=models.CharField(max_length=45)
    object=UserManager() 
    
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['username']

    def __str__(self):
        return self.username

       
class Message(models.Model):
   sender=models.ForeignKey(Useremail,on_delete=models.SET_NULL,null=True,blank=True)
   recipient=models.ForeignKey(Useremail,on_delete=models.SET_NULL,null=True,blank=True,related_name="messages")
   subject=models.CharField(max_length=50)
   body=models.TextField()
   created_on=models.DateTimeField(auto_now_add=True)

   def __str__(self):
     return self.subject




class Emailhistory(models.Model):
   sender=models.EmailField(blank=True)
   recipient=models.EmailField(blank=True)
   subject=models.CharField(max_length=50)
   body=models.TextField()
   created_on=models.DateTimeField(auto_now_add=True)

   def __str__(self):
     return self.subject





