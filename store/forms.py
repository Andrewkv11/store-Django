from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name  (ex. user1)'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email  (ex. user1@mail.ru)'}))
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Password (minimum of 8 characters, with letters and number)'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Password'}))
