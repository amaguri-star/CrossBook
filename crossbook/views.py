from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import CreateUserForm, CreatePostForm


# Create your views here.
def home(request):
    return render(request, 'crossbook/home.html')


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, username + "のアカウントが作成されました")
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'crossbook/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'ユーザー名かパスワードのどちらかが間違っています。')
    context = {}
    return render(request, 'crossbook/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('login')


def profile(request, pk):
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    context = {"user": user, 'posts': posts}
    return render(request, 'crossbook/profile.html', context)


def sell(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile', request.user.id)
    else:
        form = CreatePostForm()

    context = {'form': form}
    return render(request, 'crossbook/sell.html', context)


