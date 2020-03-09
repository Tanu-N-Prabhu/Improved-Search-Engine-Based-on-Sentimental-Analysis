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
import re
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob
from search_engine_project.logger import log
from search_engine_app.validations import validation







class SearchWeb:

    def __init__(self,topic,sentiment="",num=50,stop=50,final_output={},sentiment_dict={}):
        self.topic=topic
        self.final_output=final_output
        self.sentiment=sentiment
        self.sentiment_dict=sentiment_dict
        self.num=num
        self.stop=stop
        log.debug("Search web objected created with the topic-%s , sentiment - %s and final_output-%s"%(self.topic,self.sentiment,self.final_output))

    
    def search_web(self):
        """This function takes input as any news topic and search for it in web and return website source and URL
        @Author: Adarsh Koppa Manjunath
        @Parameter:
            topic(str)- News topic user input
        @Return:
        web_result_list(list)- list of URLs"""
        web_result_list=[]
        try:
            web_results=search(self.topic,lang="en",num=self.num,stop=self.stop,pause=1)
            for index in web_results:
                if index.endswith((".pdf",".docx",".ppt")):
                    log.debug("URL with extensions ignored-%s"%(index))
                    pass
                else:
                    web_result_list.append(index)
            return web_result_list

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
            return web_result_list



    def extract_content(self,url):
        """This function takes URL as input and parse it to beautiful soup library to extract content and also clean it at the primary level with basic blacklist filter
        @Source: https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
        @Parameter:
            URL(str)- needs to be extracted
        @Return:
            text(str)- extracted text"""
        try:
            sentiment=""
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

            text=self.clean_text(text)
            if self.sentiment!="na":
                positive,negative=self.sentiment_analysis(text)
                log.debug("\n URL:%s \n Positive-%s \n Negative-%s"%(url,positive,negative))
                if sentiment =="negative":
                    self.sentiment_dict[url]=negative
                    log.debug(self.sentiment_dict)
                else:
                    self.sentiment_dict[url]=positive
                    log.debug(self.sentiment_dict)
            else:
                return ""
            return ""

            
        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
            return sentiment
        


    def clean_text(self,text):
        """This function is used to clean text for sentimental analysis
        @Author: Adarsh Koppa Manjunath
        @Parameters:
            text(str): text to be cleaned
        @return
            final_output(dict): url and serach result"""
        try:
            #remove square brackets
            text = re.sub('\[[^]]*\]', '', text)
            #remove digits
            pattern = r'[^a-zA-z0-9\s]'
            text=  re.sub(pattern, '', text)
            #steming the text
            ps = nltk.porter.PorterStemmer()
            text = ' '.join([ps.stem(word) for word in text.split()])
            #tokenization and stop words removal
            tokenizer = ToktokTokenizer()
            stopword_list = set(stopwords.words('english'))
            tokens = tokenizer.tokenize(text)
            tokens = [token.strip() for token in tokens]
            filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
            return filtered_tokens

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
            return "exception: failed"

    def sentiment_analysis(self,text):
        """this function used to know the sentiment of text
        @Author: Adarsh Koppa Manjunath
        @Parameter:
            text(list): list of words
        @return:
            sentiment(string): Postive or Negative"""
        try:
            pos_count=0
            pos_correct=0
            for word in text:
                analysis = TextBlob(word)
                if analysis.sentiment.polarity > 0:
                    pos_correct += 1
                pos_count +=1
            #log.debug("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
            
            neg_count = 0
            neg_correct = 0
            
            for word in text:
                analysis = TextBlob(word)
                if analysis.sentiment.polarity < 0:
                    neg_correct += 1
                neg_count +=1
            #log.debug("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

            return (int(pos_correct/pos_count*100.0), int(neg_correct/neg_count*100.0))

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
            return "exception failed"

    def order_output(self):
        log.debug("before -ordering %s"%(self.sentiment_dict))
        self.sentiment_dict={url: value for url, value in sorted(self.sentiment_dict.items(), key=lambda item: item[1])}
        log.debug("after -ordering %s"%(self.sentiment_dict))
        temp={}
        temp=self.final_output
        self.final_output={}
        for key in self.sentiment_dict.keys():
            if temp[key]:
                self.final_output[key]=temp[key]
        return self.final_output



    
    def thread_func(self):
        """This function takes topic to be searched on web. First step will  be getting the list of URLs and second is thred function to extract content
        @Author: Adarsh Koppa Manjunath
        @Parameter:
        topic(str)- to be searched on web
        @Return:
        final_output(Dict): consists URL as key and Description as value
        """
        try:
            langobj=validation()
            lang=langobj.isEnglish(self.topic)
            if lang==False:
                print("Oops! entered topic is not in English! we support only English language at the moment")
                return "Oops! entered topic is not in English! we support only English language at the moment"

            web_result_list=self.search_web()
            log.debug("List of URLs-%s"%(web_result_list))
            threads = [threading.Thread(target=self.extract_content, args=(url,)) for url in web_result_list]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            log.debug("final output from search file-%s"%(self.final_output))
            if self.sentiment!="na":
                self.order_output()

            return self.final_output

        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
            return self.final_output