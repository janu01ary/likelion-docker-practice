from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {'post':post})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', str(post.id))
    else:
        form = PostForm()
        return render(request, 'form.html', {'form':form})

def update(request, id):
    post = get_object_or_404(Post, pk = id)
    form = PostForm(request.POST, request.FILES, instance=post)
    if request.user == post.author:
        if request.method == 'POST':
            updated_form = PostForm(request.POST, request.FILES, instance=post)
            if updated_form.is_valid():
                form.save()
                return redirect('detail', str(post.id))
        return render(request, 'form.html', {'form':form})
    raise PermissionDenied

def delete(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.user == post.author:
        post.delete()
        return redirect('home')
    raise PermissionDenied
