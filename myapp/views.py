from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth

def firstpage(request):
    return render(request, 'firstpage.html')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    posts = Post.objects

    context = {
        'posts':posts,
    }
    return render(request, 'home.html', context)


def signup(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                return redirect('login')
        except:
            return render(request,'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pass']
        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def search(request):
    postName = request.POST['postName']
    post = Post.objects.filter(title__icontains=postName)
    context = {
        'posts':post,
    }
    return render(request, 'home.html', context)

def createPost(request):
    if request.method == 'GET':
        return render(request, 'createPost.html')
    else:
        post = Post()
        title = request.POST['title']
        body = request.POST['body']
        post.title = title
        post.body = body
        post.save()
        return redirect('home')

def delete(request, postTitle):
    postName = postTitle
    post = Post.objects.get(title=postName)
    post.delete()
    return redirect('home')