from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    news = Post.objects.all()
    if len(news) > 0:
        news = Post.objects.all()
    else:
        news = {}
    return render(request, 'skSite/index.html', {'news': news, })


class PostDetailView(DetailView):
    context_object_name = 'post_list'
    template_name = 'skSite/post_detail.html'
    queryset = Post.objects.all()


class PostListView(ListView):
    model = Post
    template_name = 'skSite/all_news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def all_news(request):
    news = Post.objects.all()
    if len(news) > 0:
        news = Post.objects.all()
    else:
        news = {}
    return render(request, 'skSite/all_news.html', {'news': news, })


def faq_info(request):
    return render(request, 'skSite/faq_info.html', {})





