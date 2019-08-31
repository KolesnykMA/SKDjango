from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, redirect

send_mail(
    'Subject here',
    'Here is the message.',
    settings.EMAIL_HOST_USER,
    ['maxymura@example.com'],
    fail_silently=False,
)

from .models import Post, Document

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
        news = Post.objects.all().order_by('-id')[:3]
    else:
        news = {}

    if request.method == "POST":
        name = request.POST['name']
        from_email = request.POST['email']
        telegram = request.POST['tg']
        message = settings.EMAIL_HOST_USER
        send_mail(name, message, from_email, ['maxymura@gmail.com'], fail_silently=False)

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
        news = Post.objects.all().order_by('-id')[:3]
    else:
        news = {}
    return render(request, 'skSite/all_news.html', {'news': news, })


def faq_info(request):
    return render(request, 'skSite/faq_info.html', {})


def orgs(request):
    return render(request, 'skSite/orgs.html', {})


def docs(request):
    docs = Document.objects.all().order_by('-id')
    return render(request, 'skSite/docs.html', {'docs':docs, })


def successView(request):
    return HttpResponse('Дякую, запит відпарвлено!')