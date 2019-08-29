from django.contrib import admin

# Register your models here.

from .models import Post, Document

admin.site.register(Post)
admin.site.register(Document)
