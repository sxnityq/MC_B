from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Window, F
from django.db.models.functions import RowNumber
from django.db.models.query import QuerySet

from rest_framework.response import Response

from .serializers import (NewsSerializer, CustomUserSerializer,
                          AlbumSerializer, AlbumElementSerilaizer, AlbumElementSlugSerilaizer)
from .models import Album, NewsItem, CustomUser, AlbumElement
# Create your views here.


def home(request):  
     return render(request, template_name="main/testregister.html")


class Home(generics.GenericAPIView):
     
     permission_classes = (IsAuthenticated, )
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all().order_by('-creation_date')
    
     def get(self, request, *args, **kwargs):
          queryset = self.filter_queryset(self.get_queryset())

          page = self.paginate_queryset(queryset)
          if page is not None:
               serializer = self.get_serializer(page, many=True)
               return self.get_paginated_response(serializer.data)

          serializer = self.get_serializer(queryset, many=True)
          return Response(serializer.data)
     
 
class SoloNew(generics.RetrieveAPIView):
     
     permission_classes = (IsAuthenticated, )
     lookup_field = 'slug'
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()


class UserRegistrationBackend(generics.CreateAPIView):
     
     serializer_class = CustomUserSerializer
     queryset = CustomUser.objects.all()


class GetAlbumApi(generics.RetrieveAPIView):
     
     lookup_field = 'slug'
     serializer_class = AlbumElementSlugSerilaizer
     queryset = Album.objects.all()


class AlbumListApi(generics.ListAPIView):

     serializer_class = AlbumSerializer
     queryset = Album.objects.all()
