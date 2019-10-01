from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, redirect

from .models import Post, Document, Slider

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    news = Post.objects.all()
    slides = Slider.objects.all()
    if len(news) > 0:
        news = Post.objects.all().order_by('-id')[:3]
    else:
        news = {}

    if len(slides) > 0:
        slides = Slider.objects.all().order_by('-id')
    else:
        slides= {}

    if request.method == "POST":
        send_mail(
            request.POST['name'],
            'Sent from ' + request.POST['email'] + " Telegram " + request.POST['tg'] + request.POST['message'],
            settings.EMAIL_HOST_USER,
            ['sknaukma@ukma.edu.ua'],
            fail_silently=False,
        )

    return render(request, 'skSite/index.html', {'news': news, 'slides': slides, })


class PostDetailView(DetailView):
    context_object_name = 'post_list'
    template_name = 'skSite/post_detail.html'
    queryset = Post.objects.all()


class PostListView(ListView):
    model = Post
    template_name = 'skSite/all_news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


def faq_info(request):
    return render(request, 'skSite/faq_info.html', {})


def orgs(request):
    return render(request, 'skSite/orgs.html', {})


def docs(request):
    docs = Document.objects.all().order_by('-id')
    return render(request, 'skSite/docs.html', {'docs':docs, })


def successView(request):
    return HttpResponse('Дякую, запит відпарвлено!')