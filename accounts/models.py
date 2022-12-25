
#from django.contrib.auth.models import UserManager
from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

# Create your models here.
class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=45)
    created_on=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=45)
    lastname=models.CharField(max_length=45)
    #object=UserManager()
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['username']

    def __str__(self):
        return self.username


class AuthTokens(models.Model):
    token= models.CharField(max_length=1000)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    isExpired=models.BooleanField(default=False)

    def __str__(self):
        return self.token


# class User(AbstractUser):
#     email=models.EmailField(unique=True)
#     username=models.CharField(max_length=45)
#     created_on=models.DateTimeField(auto_now_add=True)
#     firstname=models.CharField(max_length=45)
#     lastname=models.CharField(max_length=45)
    
    

#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS =['username']

#     def __str__(self):
#         return self.username

 



