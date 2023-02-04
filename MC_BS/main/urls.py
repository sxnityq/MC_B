from django.urls import path


from .views import Home, SoloNew, UserRegistrationBackend, GetAlbumApi, home

urlpatterns = [
    path('api/v1/', view=Home.as_view()),
    path('api/v1/<slug:slug>/', view=SoloNew.as_view()),
    path('api/v1/registrate/', view=UserRegistrationBackend.as_view()),
    path('api/v1/album/<slug:slug>/', view=GetAlbumApi.as_view()),
    path('test', view=home)
]
