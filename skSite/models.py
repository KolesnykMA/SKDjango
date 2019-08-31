from django.utils import timezone

from django.db import models

# Create your models here.


class Post(models.Model):
    post_head = models.CharField(max_length=100)
    post_text = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='news_images')
    date_posted = models.DateTimeField(default=timezone.now)


class Document(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents_pdfs')