"""server2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from capstone_db import db_views
from eth_api import eth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', db_views.UserViewSet)
router.register(r'picture', db_views.PictureViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'user', db_views.UserViewSet),
    # url(r'picture', db_views.PictureViewSet),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^eth/check', eth_views.check_account), #지갑있는지 확인
    url(r'^eth/make', eth_views.make_account), #지갑만들기
    url(r'^eth/mining', eth_views.mining),
]
