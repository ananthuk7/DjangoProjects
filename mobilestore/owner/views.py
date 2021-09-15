from django.shortcuts import render, redirect
from owner import forms
from owner.models import Mobiles, Order
from django.db.models import Count


# Create your views here.
def add_mobile(request):
    form = forms.MobileAddForm()
    context = {'form': form}
    if request.method == 'POST':
        form = forms.MobileAddForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            # mobile_name = form.cleaned_data["mobile_name"]
            # model = form.cleaned_data['model']
            # company = form.cleaned_data['company']
            # price = form.cleaned_data['price']
            # stock = form.cleaned_data['stock']
            # mobiles = Mobiles(mobile_name=mobile_name, model=model, company=company, price=price, stock=stock)
            # mobiles.save()
            form.save()
            return redirect('viewmobile')
        else:
            return render(request, 'addmobile.html', context)
    return render(request, 'addmobile.html', context)


def view_mobiles(request):
    mobiles = Mobiles.objects.all()
    context = {"mobiles": mobiles}
    form = forms.SearchForm()
    context['form'] = form
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            mobile_name = form.cleaned_data['mobile_name']
            mobiles = Mobiles.objects.filter(mobile_name__contains=mobile_name)
            context["mobiles"] = mobiles
            context['form'] = form
            return render(request, 'viewmobiles.html', context)
        else:
            return render(request, 'viewmobiles.html', context)
    return render(request, 'viewmobiles.html', context)


def remove_item(request, id):
    mobile = Mobiles.objects.get(id=id)
    mobile.delete()
    return redirect('viewmobile')


def update_mobile(request, id):
    mobile = Mobiles.objects.get(id=id)
    # data = {
    #     'mobile_name': mobile.mobile_name,
    #     'model': mobile.model,
    #     'company': mobile.company,
    #     'price': mobile.price,
    #     'stock': mobile.stock
    # }
    form = forms.MobileUpdateForm(instance=mobile, files=request.FILES)
    context = {'form': form}
    if request.method == 'POST':
        form = forms.MobileUpdateForm(request.POST, instance=mobile, files=request.FILES)
        context['form'] = form
        if form.is_valid():
            # mobile.mobile_name = form.cleaned_data["mobile_name"]
            # mobile.model = form.cleaned_data['model']
            # mobile.company = form.cleaned_data['company']
            # mobile.price = form.cleaned_data['price']
            # mobile.stock = form.cleaned_data['stock']
            # mobile.save()
            form.save()
            return redirect('viewmobile')
        else:
            return render(request, 'updatemobile.html', context)
    return render(request, 'updatemobile.html', context)


def mobile_details(request, id):
    mobiles = Mobiles.objects.get(id=id)
    context = {"mobile": mobiles}
    return render(request, 'mobiledetails.html', context)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def dashboard(request):
    orders = Order.objects.filter(status="ordered")
    mobile = Order.objects.values("products__mobile_name").annotate(count=Count('products'))
    deliver = Order.objects.filter(status="Delivered")
    cancel = Order.objects.filter(status="cancelled")
    copie = Mobiles.objects.all()

    context = {'orders': orders, 'reports': mobile, 'delivers': deliver, 'cancelled': cancel, 'copies': copie}
    return render(request, 'dashboard.html', context)


def order_edit(request, id):
    order = Order.objects.get(id=id)
    form = forms.OrderEdit(instance=order)
    if request.method == 'POST':
        form = forms.OrderEdit(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'orderedit.html', {'form': form})
    return render(request, 'orderedit.html', {'form': form})
