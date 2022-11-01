from django.db import models

# Create your models here.

#creates a databse named Url which has 2 tables, one names link which keeps track of the link we are passed in (max length of 10000) and 
#and one called uuid with keeps track of the link's generated id (max length of 10)
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)