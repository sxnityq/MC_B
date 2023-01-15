from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import NewsItem, CustomUser

class NewsSerializer(ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ("title", "slug", "descr", "image", "creation_date")


class CustomUserSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        print(attrs)
        return attrs
    
    class Meta:
        model = CustomUser
        fields = ("email", "username", "password")