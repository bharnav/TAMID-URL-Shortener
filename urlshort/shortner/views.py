from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.

#renders our home/index page
def index(request):
    return render(request, 'index.html')

#creates the URL we pass in in our database and sends back a response with the URL's id
def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

#redirects us from our shortened URL to our original URL
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)