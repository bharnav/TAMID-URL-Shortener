from django.urls import path
from . import views

#keeps track of all of the URLs that our web app can route to, such as the index page via index(), a request for an id for a URL via create(), going from our
#shortened URL to the URL that we passed via go()
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]