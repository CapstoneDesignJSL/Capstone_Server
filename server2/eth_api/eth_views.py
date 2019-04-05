from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from capstone_db.models import User

def check_account(request):

    user_email = 'jsltest@gmail.com' #클라에서 요청하는걸로 변경

    try:
        queryset = User.objects.get(email_txt=user_email)
        print(queryset.email_txt)
        return HttpResponse('true')
    except:
        return HttpResponse('false')
    pass


def make_account(request):

    return HttpResponse('true')


def mining(request):

    pass