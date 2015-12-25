from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import datetime

class dreamDB(models.Model):
    title = models.CharField(max_length=100)
    dream = models.CharField(max_length=3000)
    mood = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    user = models.CharField(max_length=100,default="unknown user")
    datetime = models.DateTimeField(default=datetime.datetime.now())

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'

class Likes(models.Model):
    user = models.CharField(max_length=100,null=True,blank=True)
    postid = models.IntegerField(null=True,blank=True)
