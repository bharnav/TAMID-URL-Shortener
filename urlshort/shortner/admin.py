from django.contrib import admin
from .models import Url

# Register your models here.

#imports our model and then registers it as a new database
admin.site.register(Url)