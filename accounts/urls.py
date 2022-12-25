from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("signup/",SignupClass.as_view()),
    path("login/",LoginView.as_view()), 
    path("forgotpassword/",ForgotPassword.as_view()),
    path("newpassword/<int:id>/",NewPassword.as_view()), 
    path("forgetpasswordforuser/<int:id>/<str:token>",ForgotPassword.as_view()), 
]
