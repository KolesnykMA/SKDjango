from django.utils import timezone

from django.db import models

# Create your models here.


class Post(models.Model):
    post_head = models.CharField(max_length=128)
    post_short_body = models.CharField(max_length=256)
    post_text = models.TextField(max_length=3000)
    author = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='news_images')
    date_posted = models.DateTimeField(default=timezone.now)


class Document(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    doc_name = models.CharField(max_length=100)
    doc_description = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents_pdfs')


class Slider(models.Model):
    slider_text = models.CharField(max_length=100)
    file = models.ImageField(default='default.jpg', upload_to='slider_img')