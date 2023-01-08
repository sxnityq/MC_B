from django.urls import path


from .views import Home, SoloNew

urlpatterns = [
    path('', view=Home.as_view()),
    path('<slug:slug>/', view=SoloNew.as_view()),
]
