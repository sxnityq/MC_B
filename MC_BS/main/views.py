from django.shortcuts import render, HttpResponse
from rest_framework import generics

from .serializers import NewsSerializer
from .models import NewsItem
# Create your views here.


class Home(generics.ListAPIView):
     
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()