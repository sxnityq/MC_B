from rest_framework.serializers import ModelSerializer

from .models import NewsItem

class NewsSerializer(ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ("title", "slug", "descr", "image", "creation_date")
    