from django.shortcuts import render, redirect
from customer.forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from owner.models import Book, Order
from customer import forms
from customer.filters import BookFilter
from customer.decorators import user_signin_required


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


# @user_signin_required
def home(request, *args, **kwargs):
    books = Book.objects.all()
    context = {}
    context['books'] = books
    return render(request, 'customer/base.html', context)


def signout(request, *args, **kwargs):
    logout(request)
    return redirect('home')


@user_signin_required
def order_view(request, id, *args, **kwargs):
    book = Book.objects.get(id=id)
    form = forms.OrderForm()
    context = {'form': form}
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            book.no_of_copies -= 1
            book.save()
            return redirect('home')
        else:
            return render(request, 'customer/orderview.html', {'form': form})
    return render(request, 'customer/orderview.html', context)


@user_signin_required
def order_details(request, *args, **kwargs):
    orders = Order.objects.filter(user=request.user).exclude(status='cancelled')
    context = {'orders': orders}
    return render(request, 'customer/orderdetails.html', context)


@user_signin_required
def cancel_order(request, id, *args, **kwargs):
    order = Order.objects.get(id=id)
    order.status = 'cancelled'
    order.save()
    return redirect('home')


@user_signin_required
def find_book(request, *args, **kwargs):
    filters = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'customer/search_books.html', {'filters': filters})
