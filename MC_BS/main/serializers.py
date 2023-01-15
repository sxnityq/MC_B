from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import NewsItem, CustomUser, Album

class NewsSerializer(ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ("title", "slug", "descr", "image", "creation_date")


class CustomUserSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        print(attrs)
        return attrs
    
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ("email", "username", "password1", "password2")
        

class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = ("title", "slug", "description")    