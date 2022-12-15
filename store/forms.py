from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username  (ex. user1)'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First name  (ex. Alex)'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last name  (ex. Smith)'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email  (ex. user1@mail.ru)'}))
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input', 'placeholder': 'Password (minimum of 8 characters, with letters and number)'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Password'}))
