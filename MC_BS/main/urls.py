from django.urls import path


from .views import Home, SoloNew, UserRegistrationBackend

urlpatterns = [
    path('', view=Home.as_view()),
    path('<slug:slug>/', view=SoloNew.as_view()),
    path('api/v1/registrate/', view=UserRegistrationBackend.as_view())
]
