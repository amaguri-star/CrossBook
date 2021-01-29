from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="ユーザー名", max_length=20)
    email = forms.EmailField(label="メールアドレス", max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']