import logging
import traceback
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from search_engine_app.forms import ContactForms
from search_engine_app.search_web import SearchWeb
from search_engine_project.logger import log
from search_engine_app.forms import radioButtons
from django.contrib import messages
# Create your views here.


def search(request):
    """This function communicates between template and search_web files"""
    try:
        if request.method=="POST":
            
            form = ContactForms(request.POST)
            form1 = radioButtons(request.POST)
            if form.is_valid():
                topic=form.cleaned_data['name']
                
                log.debug("\n topic to be searched-%s"%(topic))
                sentiment="positive"
                search_web_obj=SearchWeb(topic,final_output={},sentiment="positive",sentiment_dict={})
                result=search_web_obj.thread_func()
                
                log.debug("\n final result recevied in views.py %s"%(result))
                return render(request,"results.html",{'result':result,'sentiment':sentiment})


            elif form1.is_valid():
                name1 = form1.cleaned_data['options']
                print(name1)
                messages.success(request, 'The sentiment you selected was: {}'.format(name1))

            

        form = ContactForms()
        form1 = radioButtons()
        
        return render(request,"home.html",{'form1':form1, 'form': form}) 

    except Exception as e:
        log.error('An exception occurred: {}'.format(e))
        log.error(traceback.format_exc())
        
        
        
def ise(request):
    return render(request, "ise.html")

def projectTeam(request):
    return render(request, "projectTeam.html")


        
            
   
        
