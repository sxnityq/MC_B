from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.db.models.query import QuerySet

from rest_framework.response import Response

from .serializers import NewsSerializer, CustomUserSerializer, AlbumSerializer, AlbumElementSerilaizer
from .models import Album, NewsItem, CustomUser
# Create your views here.


def home(request):
     
     return render(request, template_name="main/testregister.html")


class Home(generics.GenericAPIView):
     
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
     lookup_field = 'slug'
     serializer_class = NewsSerializer
     queryset = NewsItem.objects.all()


class UserRegistrationBackend(generics.CreateAPIView):
     
     serializer_class = CustomUserSerializer
     queryset = CustomUser.objects.all()


class GetAlbumApi(generics.GenericAPIView):
     
     lookup_field = 'slug'
     serializer_class = AlbumElementSerilaizer
     queryset = Album.objects.all()
     
     def get(self, request, *args, **kwargs):
          
          instance = self.get_object()
          queryset = instance.albumelement_set.all()
          page = self.paginate_queryset(queryset)
          if page is not None:
               serializer = self.get_serializer(page, many=True)
               return self.get_paginated_response(serializer.data)

          serializer = self.get_serializer(queryset, many=True)
          return Response(serializer.data)


class AlbumListApi(generics.ListAPIView):
     
     serializer_class = AlbumSerializer
     queryset = Album.objects.all()