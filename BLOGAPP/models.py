from turtle import title
from django.db import models

# Create your models here.
class Article(models.Model):
    '''Creating the task table in my database''' 
    name = models.CharField(max_length=400)
    date_created = models.DateField(auto_now_add= True)
    body = models.TextField()
    
    def __str__(self):
        return self.name