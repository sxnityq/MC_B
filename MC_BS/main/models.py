from django.db import models
from django.utils.text import slugify

from .utils import upload_image

# Create your models here.


class NewsItem(models.Model):
    
    title = models.CharField(verbose_name='title field', unique=True,
                             null=False, blank=False, max_length=64)
    slug = models.SlugField(verbose_name='slug field', unique=True,
                            null=False, blank=False)
    descr = models.TextField(verbose_name="description", blank=True, max_length=4096)
    image = models.ImageField(verbose_name="post image", upload_to=upload_image)
    
    creation_date = models.DateTimeField(verbose_name="date of creating",
                                         auto_now_add=True)
    
