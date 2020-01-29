from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import forms
from search_engine_app.tests import search_web


# Create your views here.
class ContactForms(forms.Form):
    name=forms.CharField(label = '')
    
def search(request):
    if request.method=="POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            result=search_web(name)
            return render(request,"results.html",{'result':result})
    form = ContactForms()
    return render(request,"home.html",{'form':form}) # do some research what it does
         