#import logger
from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from search_engine_app.forms import ContactForms
from search_engine_app.tests import thread_func


# Create your views here.

    
def search(request):
    if request.method=="POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            result=thread_func(name)
            return render(request,"results.html",{'result':result})
    form = ContactForms()
    return render(request,"home.html",{'form':form}) # do some research what it does
         