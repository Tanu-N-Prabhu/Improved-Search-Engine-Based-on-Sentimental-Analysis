
from pytrends.request import TrendReq
from search_engine_app.models import Trendingtopics
from datetime import date
import re


class TrendingTopics:
    
    def trending_topics(self):
           
            pytrends = TrendReq(hl='en-US', tz=360)
            df=pytrends.trending_searches(pn='canada')
            trending_topics_str=df[0].to_string().replace("\n","")
            trending_topics_str=re.sub(r"[0-9]+","",trending_topics_str)
            exsiting_trend=Trendingtopics.objects.all()[0]

            if trending_topics_str==exsiting_trend:
                return trending_topics
            else:
                trending_topicobj=Trendingtopics(trending_topics=trending_topics_str)
                trending_topicobj.save()
                datetoday=str(date.today())
                return ("Trending topic updated as on"+datetoday+"\n"+trending_topics_str)
                




        