# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializers, PictureSerializers
from .models import User, Picture


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #     pass
    pass


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializers
    pass


def img_upload(request):
    pass
