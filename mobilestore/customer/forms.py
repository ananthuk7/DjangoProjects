
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from owner.models import Order
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['products', 'address', 'phone']
        widgets = {
            'products': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'address': forms.Textarea(attrs={'class': 'form-control'})

        }
