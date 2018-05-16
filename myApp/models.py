from django.db import models
from django.utils import timezone 

class Blog(models.Model):
    poster = models.CharField(max_length=100)
    postname = models.CharField(max_length=50)
    post = models.TextField(max_length=500,default="Write a post")
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post
