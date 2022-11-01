from django.apps import AppConfig

#setting the name of our Django application to shorner
class ShortnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shortner'
