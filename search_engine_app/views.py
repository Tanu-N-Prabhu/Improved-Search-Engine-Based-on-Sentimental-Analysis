import logging
import traceback
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from search_engine_app.forms import GeneralForms
from search_engine_app.forms import userPortalForms
#from search_engine_app.forms import loginForm
from search_engine_app.search_web import SearchWeb
from search_engine_project.logger import log
from django.contrib import messages
#from search_engine_app.forms import signUpForm
from django.db import models
from django.contrib.auth.models import User
from search_engine_app.user_permissions import Authentication
#from search_engine_app.trending_topics import TrendingTopics
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



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
                    args = {'result': result}

                    return render(request, "alert.html", args)
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

def viewYourUpdatedResult(request):
   

    
    return render(request, "viewYourUpdatedResults.html")


def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			uname = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for '+ uname )

			return redirect('login')
	context = {'form': form}
	return render(request, 'register.html', context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
        

		user = authenticate(request, username = username, password = password )

		if user is not None:
			login(request, user)
			return redirect('userPortal.html')

	context = {}
	return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

def trending(request):
    if request.method=="GET":
        trendingObj=TrendingTopics()
        trending_res=trendingObj.trending_topics()
        trending_res={'trending_res':trending_res}
        return render(request,"trending.html",trending_res)


def userPortal(request):
    if request.method=="POST":
            
            form3 = userPortalForms(request.POST)

            if form3.is_valid():
                topic = form3.cleaned_data['topic']
                sentiment = form3.cleaned_data['options']
                subject=Publisher()
                status=subject.add_newsreader(request.user,topic,sentiment)
                notification=subject.notify()
                print(notification)
                messages.success(request, status)
           
            
    form3 = userPortalForms()
        
        
    return render(request,"userPortal.html",{'form': form3}) 







   
        
