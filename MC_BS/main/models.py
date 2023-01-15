from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        AbstractUser, PermissionsMixin)

from .utils import upload_image, upload_user_profile_image, upload_albom_element_image

# Create your models here.


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, password):
        
        if not email:
            raise ValueError("email field must be specified")
        if not username:
            raise ValueError("username field must be specified")
        
        user = self.model(email=self.normalize_email(email),
                          username=username)
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(PermissionsMixin, AbstractBaseUser):
    
        email = models.EmailField(verbose_name="email field", unique=True,
                                  max_length=64, db_index=True)
        username = models.CharField(verbose_name="username field", unique=True,
                                    max_length=32, db_index=True)
        profile_image = models.ImageField(verbose_name="user profile image",
                                          upload_to=upload_user_profile_image)
        data_joined = models.DateTimeField(verbose_name="date when user join us",
                                           auto_now_add=True)
        is_active = models.BooleanField(verbose_name="active", default=True)
        is_staff = models.BooleanField(verbose_name="staff", default=False)
        is_superuser = models.BooleanField(verbose_name="admin", default=False)
        objects = CustomUserManager()
        
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']
        

class NewsItem(models.Model):
    
    title = models.CharField(verbose_name='title field', unique=True,
                             null=False, blank=False, max_length=64)
    slug = models.SlugField(verbose_name='slug field', unique=True,
                            null=False, blank=False)
    descr = models.TextField(verbose_name="description", blank=True, max_length=4096)
    image = models.ImageField(verbose_name="post image", upload_to=upload_image)
    
    creation_date = models.DateTimeField(verbose_name="date of creating",
                                         auto_now_add=True)
    
    def __str__(self):
        return self.title

    
class Album(models.Model):
        
    title = models.CharField(verbose_name="album name", unique=True,
                             null=True, max_length=64)
    slug = models.SlugField(verbose_name="album slug", unique=True,
                            null=False, blank=False)
    description = models.TextField(verbose_name="Album description", max_length=512)

    def __str__(self):
        
        return self.title


class AlbumElement(models.Model):
    
    image = models.ImageField(verbose_name='album image element',
                              upload_to=upload_albom_element_image)
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return f"image for album {Album}"