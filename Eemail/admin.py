from django.contrib import admin
from .models import Emailhistory,Message,Useremail
admin.site.register(Useremail)
admin.site.register(Message)
admin.site.register(Emailhistory)
