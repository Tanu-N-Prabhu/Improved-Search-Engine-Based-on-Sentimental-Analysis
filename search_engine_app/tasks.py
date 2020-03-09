from background_task import background
from django.contrib.auth.models import User
from search_engine_app.models import UserPortal
from search_engine_app.search_web import SearchWeb





@background(schedule=5)
def check_event(self):
        # lookup user by id and send them a message
        from search_engine_app.observer_pattern.subject_topic import Publisher
        notifobj=Publisher()
        notif_dict=notifobj.notify_dict
        db=UserPortal.objects.all()
        
        
        for index in db:
                topic=index.topic
                serach_obj=SearchWeb(topic,sentiment="na",num=5, stop=5, final_output={},sentiment_dict={})
                search_result=serach_obj.thread_func()
                url_list=search_result.keys()
        
                if index.urls == str(list(url_list)):
                        notif_dict[index.username]=False
                else: 
                        index.urls=str(list(url_list))
                        index.save(update_fields=['urls'])
                        notfi_dict[index.username]=str(list(url_list))

        return notfi_dict           

change=check_event(repeat=2)



        