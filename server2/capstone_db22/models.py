# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datashape import unicode
from django.db import models

# Create your models here.


class User(models.Model):
    email_txt = models.CharField(max_length=100, primary_key=True)
    wallet = models.CharField(max_length=100, default=None)
    balance = models.FloatField(max_length=None, default=None)

    def __unicode__(self):
        return unicode(self.email_txt) 
    
    def __str__(self):
        return str(self.wallet) #test
    pass


class Picture(models.Model):
    file_hash = models.CharField(max_length=100,primary_key=True,default=None)
    # wallet = models.CharField(max_length=100, on_delete=models.PROTECT)
    picture_name = models.CharField(max_length=20,default=None)
    image = models.ImageField(default='/default_image.png')
    price = models.IntegerField(default=None)
    author = models.CharField(max_length=100,default=None)
    wallet = models.CharField(max_length=100, default=None)

    #upload_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.picture_name)
    #
    # def __str__(self):
    #     return self.picture_binary
    pass



# class PictureInfo(models.Model):
#     picture_name = models.CharField(max_length=100,default=None)
#     category = models.CharField(max_length=10, default=5)
#     width = models.IntegerField(default=None)
#     height = models.IntegerField(default=None)
#     explanation = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.picture_name
#
#     pass


