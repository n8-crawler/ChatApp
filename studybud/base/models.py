from django.db import models
from django.contrib.auth.models import User
'''
ALL room have a topic 
All topic has messages
topic--> room 1:1 relation
topic--> many:1 reltion
'''
class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) ->str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)# topic will be set null
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created','-updated']

    def __str__(self) -> str:
        return self.name
    
class Messages(models.Model):
    """if a room is deleteed all messages for the room will be deleted
    if user is deleted all messages of user will be deleted as well"""
    room = models.ForeignKey(Room,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # preview of 50 chars will be shown as messages
    def __str__(self) -> str:
        return self.body[:50]