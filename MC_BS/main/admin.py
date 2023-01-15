from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewsItem, CustomUser, Album, AlbumElement

class CustomUserAdmin(UserAdmin):
    
    list_display = ["email", "username"]
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(NewsItem)
admin.site.register(Album)
admin.site.register(AlbumElement)
