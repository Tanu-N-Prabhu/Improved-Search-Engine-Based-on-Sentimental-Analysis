import traceback
from googlesearch import search
import requests
import threading
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import time
from multiprocessing import Pool
from google import google
from textblob import TextBlob
from search_engine_project.logger import log


class SearchWeb:

    def __init__(self,topic,final_output={}):
        self.topic=topic
        self.final_output=final_output
        log.debug("Search web objected created with the topic-%s and final_output-%s"%(self.topic,self.final_output))

    
    def search_web(self):
        """This function takes input as any news topic and search for it in web and return website source and URL
        @Author: Adarsh Koppa Manjunath
        @Parameter:
            topic(str)- News topic user input
        @Return:
        web_result_list(list)- list of URLs"""
        try:
            web_result_list=[]
            web_results=search(self.topic,lang="en",num=10,stop=10,pause=1)
            for index in web_results:
                web_result_list.append(index)
            return web_result_list

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())



    def extract_content(self,url):
        """This function  ion takes URL as input and parse it to beautiful soup library to extract content and also clean it at the primary level with basic blacklist filter
        @Source: https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
        @Parameter:
            URL(str)- needs to be extracted
        @Return:
            text(str)- extracted text"""
        try:
            html = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(html)
            soup = BeautifulSoup(html)
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            self.final_output[url]=text[:5000]
            return text[:1000]

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
        


    def sentimental_analysis(self):
        """This function is for finding the sentiment of the article by using TextBlob library"""




    def thread_func(self):
        """This function takes topic to be searched on web. First step will  be getting the list of URLs and second is thred function to extract content
        @Author: Adarsh Koppa Manjunath
        @Parameter:
        topic(str)- to be searched on web
        @Return:
        final_output(Dict): consists URL as key and Description as value
        """
        try:
            web_result_list=self.search_web()
            log.debug("List of URLs-%s"%(web_result_list))
            threads = [threading.Thread(target=self.extract_content, args=(url,)) for url in web_result_list]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            log.debug("final output from search file-%s"%(self.final_output))
            return self.final_output

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())