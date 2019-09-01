from django.contrib import admin

# Register your models here.

from .models import Post, Document,Slider

admin.site.register(Post)
admin.site.register(Document)
admin.site.register(Slider)

