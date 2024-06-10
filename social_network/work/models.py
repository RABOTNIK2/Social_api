from django.db import models
from django.utils import timezone

class Theme(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    image = models.TextField(default='https://avatars.mds.yandex.net/i?id=ee54224ac5c66e2f0ce002ee3d9ca1e178e490c3-12421615-images-thumbs&n=13', blank=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.login
    
class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(blank=True)
    image = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null = True)
    reaction = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text  
    
class Comment(models.Model):
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    written_to = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    



# Create your models here.
