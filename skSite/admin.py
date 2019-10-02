from django.contrib import admin

# Register your models here.

from .models import Post, Document,Slider, Mail

admin.site.register(Post)
admin.site.register(Document)
admin.site.register(Slider)
admin.site.register(Mail)

