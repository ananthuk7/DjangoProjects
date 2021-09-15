from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from owner.models import Mobiles, Order
from customer.filters import MobileFormSearch
from customer.decorators import user_authentication


# Create your views here.
def home(request):
    mobile = Mobiles.objects.all()
    context = {'mobiles': mobile}
    return render(request, 'customer/base.html', context)


def sign_in(request):
    form = forms.Login()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['Password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'inavlid username and password')
                return redirect('signin')
        else:
            return render(request, 'customer/signin.html', {'form': form})
    return render(request, 'customer/signin.html', context)


def sign_up(request):
    form = forms.UserRegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request, 'customer/signup.html', {'form': form})
    return render(request, 'customer/signup.html', context)


@user_authentication
def sign_out(request, *args, **kwargs):
    logout(request)
    return redirect('signin')


@user_authentication
def order_form(request, id, *args, **kwargs):
    mobile = Mobiles.objects.get(id=id)
    form = forms.OrderForm(initial={'products': mobile})
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            mobile.stock -= 1
            mobile.save()
            return redirect('home')
        else:
            return render(request, 'customer/orderform.html', {'form': form})
    return render(request, 'customer/orderform.html', {'form': form})


@user_authentication
def order_details(request, *args, **kwargs):
    orders = Order.objects.filter(user=request.user).exclude(status='cancelled')
    return render(request, 'customer/orderview.html', {'orders': orders})


@user_authentication
def order_cancel(request, id, *args, **kwargs):
    order = Order.objects.get(id=id)
    order.status = 'cancelled'
    order.save()
    return redirect('home')


@user_authentication
def find_mobiles(request, *args, **kwargs):
    filters = MobileFormSearch(request.GET, queryset=Mobiles.objects.all())
    return render(request, 'customer/advance.html', {'filters': filters})
