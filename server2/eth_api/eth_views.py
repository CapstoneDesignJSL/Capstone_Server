from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from capstone_db.models import User


def check_account(request):

    # user_email = 'jsltest2@gmail.com' #클라에서 요청하는걸로 변경
    user_email = request.GET.get('email', '')

    try:
        queryset = User.objects.get(email_txt=user_email)
        print('user email =', queryset.email_txt)
        print('user account = ', queryset.wallet)
        return HttpResponse('true')
    except:
        return HttpResponse('false')
    pass


def make_account(request):

    return HttpResponse('true')


def mining(request):

    pass