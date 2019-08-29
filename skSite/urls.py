from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SKDjango import settings
from . import views

from .views import PostDetailView, PostListView


urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', views.home, name='index'),
    path('all_news/', views.all_news, name='all-news'),
    path('faq_info/', views.faq_info, name='faq-info'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
