# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    email_txt = models.CharField(max_length=100, primary_key=True)
    wallet = models.IntegerField(default=None)
    balance = models.FloatField(max_length=None, default=None)

    def __unicode__(self):
        return unicode(self.email_txt) 
    
    def __str__(self):
        return self.wallet #test
    pass


class Picture(models.Model):
    wallet = models.ForeignKey(User, on_delete=models.PROTECT)
    picture_name = models.CharField(max_length=20,default=None)
    picture_binary = models.BinaryField(max_length=None)
    #upload_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(picture_name)

    def __str__(self):
        return self.picture_binary
    pass


class PictureInfo(models.Model):
    picture_name = models.ForeignKey(Picture, on_delete=models.PROTECT)
    category = models.CharField(max_length=10, default=5)
    width = models.IntegerField(default=None)  #가로, 세로를 분리할까??
    height = models.IntegerField(default=None)
    explanation = models.CharField(max_length=500) #나중에 길이 바꾸기

    def __str__(self):
        return self.picture_name

    pass


