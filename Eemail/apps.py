from django.apps import AppConfig



class EemailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Eemail'
    def ready(self):
        import  Eemail.signals.abcdsig
