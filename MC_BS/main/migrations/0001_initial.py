# Generated by Django 4.1.5 on 2023-01-08 18:35

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='title field')),
                ('slug', models.SlugField(unique=True, verbose_name='slug field')),
                ('descr', models.TextField(blank=True, max_length=4096, verbose_name='description')),
                ('image', models.ImageField(upload_to=main.utils.upload_image, verbose_name='post image')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date of creating')),
            ],
        ),
    ]
