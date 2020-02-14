import logging
import traceback
from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from search_engine_app.forms import ContactForms
from search_engine_app.search_web import SearchWeb
from search_engine_project.logger import log

# Create your views here.



def search(request):
    """This function communicates between template and search_web files"""
    try:
        if request.method=="POST":
            
            form = ContactForms(request.POST)
            if form.is_valid():
                topic=form.cleaned_data['name']
                log.debug("\n topic to be searched-%s"%(topic))
                search_web_obj=SearchWeb(topic,final_output={})
                result=search_web_obj.thread_func()
                log.debug("\n final result recevied in views.py %s"%(result))
                return render(request,"results.html",{'result':result})

        form = ContactForms()
        return render(request,"home.html",{'form':form}) 

    except Exception as e:
        log.error('An exception occurred: {}'.format(e))
        log.error(traceback.format_exc())
        