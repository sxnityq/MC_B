from django.urls import path

from .views import xyi

urlpatterns = [
    path('', view=xyi)
]
