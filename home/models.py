from django.db import models
from django.conf import settings
# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email


class Post(models.Model):
    title = models.CharField(max_length=100)
    prize = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    categogy = models.CharField(max_length=50, default="")
    direc = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    image2 = models.ImageField(null=True)


    def __str__(shell):
        return shell.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
