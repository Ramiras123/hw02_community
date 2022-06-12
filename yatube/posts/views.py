from django.shortcuts import render, get_object_or_404
from .models import Post, Group

SELECT_LIMIT = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:SELECT_LIMIT]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    template = 'posts/group_list.html'
    context = {
        'posts': posts,
        'groups': group
    }
    return render(request, template, context)
