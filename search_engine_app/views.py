from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect


# Create your views here.

def search(request):        
    if request.method == 'GET': # this will be GET now      
         return render(request,"home.html",{}) # do some research what it does
         