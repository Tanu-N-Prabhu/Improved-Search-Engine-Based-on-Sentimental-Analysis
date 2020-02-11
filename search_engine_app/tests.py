#import logger
from django.test import TestCase
from googlesearch import search
import requests
import threading
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import time
from multiprocessing import Pool
from google import google


def search_web(topic):
    """This function takes input as any news topic and search for it in web and return website source and URL
    Input:
        topic- News topic user input
    Output:
        website- web source name
        URL- web source URL"""

    web_result_list=[]
    web_results=search(topic,lang="en",num=10,stop=10,pause=1)
    #web_results = google.search(topic,1)
    for index in web_results:
        web_result_list.append(index)
    return web_result_list

def extract_content(URL):
    """This function takes URL as input and parse it to beautiful soup library to extract content and also clean it at the primary level with basic blacklist filter
    Source: https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/
    Input:
        URL- needs to be extracted
    Output:
        text- extracted text"""
    res = requests.get(URL)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
    ]
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    output="".join([s for s in output.strip().splitlines(True) if s.strip()])
    final_output[URL]=output[:5000]
    return output[:1000]

# Create your tests here.

def thread_func(topic):
    """This function takes topic to be searched on web. First step will  be getting the list of URLs and second is thred function to extract content
    Input:
    topic- to be searched on web
    Output:
    final_output(Dict): consists URL as key and Description as value
    """
    
    web_result_list=search_web(topic)
    global final_output
    final_output={}
    threads = [threading.Thread(target=extract_content, args=(url,)) for url in web_result_list]
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()
    return final_output