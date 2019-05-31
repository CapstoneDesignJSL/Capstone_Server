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
from django.conf import settings
from capstone_db import db_views
from eth_api import eth_views
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', db_views.UserViewSet)
router.register(r'picture', db_views.PictureViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^eth/wallet/',db_views.wallet),
    url(r'^eth/check/$', db_views.check_account),
    url(r'^eth/make/(?P<email>.+)', db_views.make_account),
    url(r'^eth/mining', db_views.mining),
    url(r'^eth/bal', db_views.balance),
    url(r'^info',db_views.file_info),
    url(r'^eth/mining_stop', db_views.mining_stop),
    url(r'^list/', db_views.picture_list),
    url(r'^list2/', db_views.picture_list2),
    url(r'^del/(?P<name>.+)', db_views.delete),
    url(r'^upload', db_views.img_upload),
    url(r'^down',db_views.down),
    url(r'^trans', db_views.transaction),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
