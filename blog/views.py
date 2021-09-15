from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def home(request):
    from events.models import Event
    posts = Blog.objects
    evets = Event.objects
    return render(request, 'blog/home.html',
                  {'posts': posts, 'evens': evets}
                  )


def showblog(request):
    posts = Blog.objects
    return render(request, 'blog/blog.html', {'posts': posts})

def showpost(request, post_id):
    blogentry = get_object_or_404(Blog, pk=post_id)
    posts = Blog.objects
    return render(request, 'blog/post.html',
                  {'blogentry': blogentry, 'posts': posts}
                  )
