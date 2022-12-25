from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import  Message,Useremail,Emailhistory

@receiver(post_save,sender=Message)
def sync_data(sender,instance,**kwargs):
    print(f"{instance}")
    
    emailhistory_instance=Emailhistory()
    print(f"{emailhistory_instance}")
    emailhistory_instance.sender=instance.sender
    emailhistory_instance.recipient=instance.recipient
    emailhistory_instance.subject=instance.subject
    emailhistory_instance.body=instance.body
    emailhistory_instance.save()