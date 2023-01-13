from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from .serializers import NewsSerializer
from .models import NewsItem
# Create your views here.


class Home(generics.ListAPIView):
     
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()
     
class SoloNew(generics.RetrieveAPIView):
     lookup_field = 'slug'
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()