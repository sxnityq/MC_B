from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .tokens import MyTokenObtainPairView

from .views import (Home, SoloNew, UserRegistrationBackend,
                     GetAlbumApi, home, AlbumListApi)


urlpatterns = [
    path('api/v1/auth/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/registrate/', view=UserRegistrationBackend.as_view()),
    path('api/v1/news', view=Home.as_view()),
    path('api/v1/news/<slug:slug>/', view=SoloNew.as_view()),
    path('api/v1/album/<slug:slug>/', view=GetAlbumApi.as_view()),
    path('api/v1/album/', view=AlbumListApi.as_view()),
    path('test', view=home)
]
