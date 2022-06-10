from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    templace = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts
    }
    return render(request, templace, context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]
    template = 'posts/group_list.html'
    context = {
        'posts': posts,
        'groups': group
    }
    return render(request, template, context)
