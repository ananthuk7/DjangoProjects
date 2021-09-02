from django.shortcuts import render, redirect
from customer.forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from owner.models import Book


# Create your views here.

def sign_up(request):
    form = UserRegistrationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request, 'customer/signup.html', context)
    return render(request, 'customer/signup.html', context)


def sign_in(request):
    form = LoginForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'invalid username or password')
                return redirect('signin')
        else:
            return render(request, 'customer/signin.html', {'form': form})
    return render(request, 'customer/signin.html', context)


def home(request):
    books = Book.objects.all()
    context = {}
    context['books']= books
    return render(request, 'customer/base.html', context)


def signout(request):
    logout(request)
    return redirect('signin')
