from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from .serializers import NewsSerializer, CustomUserSerializer, AlbumSerializer
from .models import NewsItem, CustomUser
# Create your views here.


def home(request):
     
     return render(request, template_name="main/testregister.html")


class Home(generics.ListAPIView):
     
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()
    
 
class SoloNew(generics.RetrieveAPIView):
     lookup_field = 'slug'
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()


class UserRegistrationBackend(generics.CreateAPIView):
     
     serializer_class = CustomUserSerializer
     queryset = CustomUser.objects.all()


class GetAlbumApi(generics.RetrieveAPIView):
     
     serializer_class = AlbumSerializer
     queryset = CustomUser.objects.all()
