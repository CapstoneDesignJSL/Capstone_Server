from .models import User, Picture2
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email_txt', 'wallet', 'balance')
    pass


class PictureSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Picture2
        fields = ('file_hash', 'picture_name', 'image', 'price','author','wallet')
    pass

#
# class PictureInfoSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PictureInfo
#         fields = ('picture_name', 'category', 'width', 'height', 'explanation')
#     pass
#
