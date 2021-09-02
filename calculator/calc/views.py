from django.shortcuts import render
from calc import forms


# Create your views here.
def home(request):
    return render(request, 'index.html')


def addition(request):
    if request.method == 'GET':
        form = forms.CalculationForm()
        context = {'form': form}
        return render(request, 'addition.html', context)
    elif request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 + num2
            # # print(res)
            context = {'result': res, 'form': form}
            return render(request, 'addition.html', context)
    return render(request, 'addition.html', {'form': form})


def sub(request):
    if request.method == 'GET':
        form = forms.CalculationForm()
        context = {'form': form}
        return render(request, 'sub.html', context)
    elif request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            if num1 < num2:
                res = num2 - num1
            else:
                res = num1 - num2

            # print(res)
            context = {'result': res, 'form': form}
            return render(request, 'sub.html', context)
        return render(request, 'sub.html', {'form': form})


def multiplication(request):
    if request.method == 'GET':
        form = forms.CalculationForm()
        context = {'form': form}
        return render(request, 'mul.html', context)
    elif request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 * num2
            # print(res)
            context = {'result': res, 'form': form}
            return render(request, 'mul.html', context)
        return render(request, 'mul.html', {'form': form})


def division(request):
    if request.method == 'GET':
        form = forms.CalculationForm()
        context = {'form': form}
        return render(request, 'div.html', context)
    elif request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            try:
                res = num1 // num2
                error = "no error"
                # print(res)
            except Exception as e:
                res = "error"
                error = e
            context = {'result': res, 'error': error, 'form': form}
            return render(request, 'div.html', context)
        return render(request, 'div.html', {'form': form})


def cube(request):
    if request.method == 'GET':
        form = forms.CubeForm()
        context = {'form': form}
        return render(request, 'cube.html', context)
    elif request.method == 'POST':
        form = forms.CubeForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            res = int(num1) ** 3
            print(res)
            context = {'result': res, 'form': form}
            return render(request, 'cube.html', context)
        return render(request, 'cube.html', {'form': form})
