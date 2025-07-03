from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def home(request):
    # We import the data of the Post
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts":posts})

def post(request, id):
    # We import the data of the Post
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {"post":post})
