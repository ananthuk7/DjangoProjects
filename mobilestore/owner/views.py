from django.shortcuts import render, redirect
from owner import forms
from owner.models import Mobiles


# Create your views here.
def add_mobile(request):
    form = forms.MobileAddForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.MobileAddForm(request.POST)
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
    context = {}
    context["mobiles"] = mobiles
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
    form = forms.MobileUpdateForm(instance=mobile)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.MobileUpdateForm(request.POST,instance=mobile)
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
    context = {}
    context["mobile"] = mobiles
    return render(request, 'mobiledetails.html', context)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
