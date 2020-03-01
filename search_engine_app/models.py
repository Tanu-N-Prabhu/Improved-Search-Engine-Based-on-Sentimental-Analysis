from django.db import models

# Create your models here.

class Feedback(models.Model):
    username=models.CharField(max_length=200)
    user_email=models.CharField(max_length=300)
    feedback=models.TextField()
    
    def __str__(self):
        return self.feedback

class Trendingtopics(models.Model):
    trending_topics=models.TextField()

    def __str__(self):
        return self.trending_topics