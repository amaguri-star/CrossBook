from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CreateUserForm, CreatePostForm, EditProfileForm, EditPostForm
from .models import Post, Profile


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


def edit_account(request):
    context = {}
    return render(request, 'crossbook/edit-account.html', context)


@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    context = {"user": user, 'posts': posts}
    return render(request, 'crossbook/profile.html', context)


@login_required(login_url='login')
def edit_profile(request, pk):
    user = User.objects.get(id=pk)
    form = EditProfileForm(instance=user.profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.id)
    context = {'form': form}
    return render(request, 'crossbook/edit-profile.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'crossbook/post-detail.html', context)


@login_required(login_url='login')
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    form = EditPostForm(instance=post)

    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', post.id)

    context = {'form': form}
    return render(request, 'crossbook/edit-post.html', context)


@login_required(login_url='login')
@require_POST
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('profile', post.author_id)
