from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns += doc_url

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)