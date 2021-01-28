from django.shortcuts import render, redirect
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
            return redirect('login')

    context = {'form': form}
    return render(request, 'crossbook/signup.html', context)


