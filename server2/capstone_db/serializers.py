from .models import User, Picture, PictureInfo
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email_txt', 'wallet', 'balance')
    pass


class PictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('wallet', 'picture_name', 'picture_binary')
    pass


class PictureInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PictureInfo
        fields = ('picture_name', 'category', 'width', 'height', 'explanation')
    pass

