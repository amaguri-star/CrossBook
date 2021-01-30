from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CreateUserForm


# Create your views here.
def home(request):
    return render(request, 'crossbook/home.html')


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, username + "のアカウントが作成されました")
            return redirect('login')

    context = {'form': form}
    return render(request, 'crossbook/signup.html', context)


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



