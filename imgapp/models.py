from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]