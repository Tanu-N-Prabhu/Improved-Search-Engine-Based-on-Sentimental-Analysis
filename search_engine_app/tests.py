from django.test import TestCase
from googlesearch import search

def search_web(topic):
    web_result_list=[]
    web_results=search(topic,lang="en",num=10,stop=10,pause=1)
    for index in web_results:
        web_result_list.append(index)
    return web_result_list
    

# Create your tests here.
