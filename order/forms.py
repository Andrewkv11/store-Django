from django import forms
from .models import Order


class OrderCreateForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'City'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))



    # class Meta:
    #     model = Order
    #     fields = [
    #         'username',
    #         'city',
    #         'address',
    #     ]
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'input'}),
    #         'city': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City'}),
    #         'address': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
    #     }

