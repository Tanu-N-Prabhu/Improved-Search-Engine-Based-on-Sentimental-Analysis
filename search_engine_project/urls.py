"""search_engine_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from search_engine_app import views
from django.conf.urls import  url, include
from search_engine_app.views import ise
from search_engine_app.views import viewYourUpdatedResult


from search_engine_app.views import projectTeam
#from search_engine_app.views import login
#from search_engine_app.views import signUp
from search_engine_app.views import loginPage
from search_engine_app.views import registerPage
from search_engine_app.views import logoutUser
from search_engine_app.views import userPortal



#from search_engine.views import search_engineView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_engine_app/',views.search),

    path('search_engine_app/home.html', views.search),
    path('search_engine_app/ise.html', views.ise),
    path('search_engine_app/projectTeam.html', views.projectTeam),
    path('search_engine_app/login.html',  views.loginPage, name = 'login'),
    path('search_engine_app/register.html',  views.registerPage),
    path("logout", logoutUser, name="logout"),
    #path('search_engine_app/signUp.html',  views.signUp),
    path("search_engine_app/trending.html",views.trending),
    path("search_engine_app/userPortal.html",views.userPortal),
    path("search_engine_app/viewYourUpdatedResults.html",views.viewYourUpdatedResult),


   

    
]


