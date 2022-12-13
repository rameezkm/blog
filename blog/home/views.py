from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from . models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    post = {
        'post':Post.objects.all()
    }
    return render(request,'index.html',post)
def post(request, id):
    post = {
        'post':Post.objects.get(id=id)
    }
    return render(request, 'post.html',post)
def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
def update(request,post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})
@login_required
def singlepost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request,'singlepost.html',{'form':PostForm()})
def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})

        
 