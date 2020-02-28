import logging
import traceback
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from search_engine_app.forms import GeneralForms
from search_engine_app.forms import loginForm
from search_engine_app.search_web import SearchWeb
from search_engine_project.logger import log
from django.contrib import messages
from search_engine_app.forms import signUpForm
from django.db import models
from django.contrib.auth.models import User

# Create your views here.


def search(request):
    """This function communicates between template and search_web files"""
    try:
        if request.method=="POST":
            
            form = GeneralForms(request.POST)

            if form.is_valid():
                topic=form.cleaned_data['name']
                sentiment = form.cleaned_data['options']
                search_web_obj=SearchWeb(topic,final_output={},sentiment=sentiment,sentiment_dict={})
                result=search_web_obj.thread_func()
                if type(result)==str:
                   return HttpResponse("<h> <font size=""3"" color=""red""> %s </font></h>"%(result))
                else:
                    args = {'result':result,'sentiment':sentiment}
                    return render(request,"results.html", args)


        form = GeneralForms()
        
        
        return render(request,"home.html",{'form': form}) 


    except Exception as e:
        log.error('An exception occurred: {}'.format(e))
        log.error(traceback.format_exc())
        
        
        
def ise(request):
    return render(request, "ise.html")

def projectTeam(request):
    return render(request, "projectTeam.html")


def login(request):
    if request.method=="POST":
            
            form1 = loginForm(request.POST)

            if form1.is_valid():
                uname = form1.cleaned_data['uname']
                pwd = form1.cleaned_data['pwd']
                print(uname)
                print(pwd)
                
                
    form1 = loginForm()
        
        
    return render(request,"login.html",{'form': form1}) 



def signUp(request):
    if request.method=="POST":
            
            form2 = signUpForm(request.POST)

            if form2.is_valid():
                newName = form2.cleaned_data['newName']
                email = form2.cleaned_data['email']
                pwd = form2.cleaned_data['pwd']
                pwdr = form2.cleaned_data['pwdr']
                try:
                    user = User.objects.create_user(newName,email,pwd)
                    user.is_staff = False
                    user.save()
                    
                except:
                    return HttpResponse("<h> <font size=""3"" color=""red""> Registration Failed!!!! Username or email address already taken </font></h>")
            form1 = loginForm()
            return render(request,"login.html",{'form': form1})
                
    form2 = signUpForm()
        
        
    return render(request,"signUp.html",{'form': form2}) 







   
        
