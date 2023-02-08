from django.urls import path, include


from .views import (Home, SoloNew, UserRegistrationBackend,
                     GetAlbumApi, home, AlbumListApi)


urlpatterns = [
    path('api/v1/news', view=Home.as_view()),
    path('api/v1/news/<slug:slug>/', view=SoloNew.as_view()),
    path('api/v1/registrate/', view=UserRegistrationBackend.as_view()),
    path('api/v1/album/<slug:slug>/', view=GetAlbumApi.as_view()),
    path('api/v1/album/', view=AlbumListApi.as_view()),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('test', view=home)
]
