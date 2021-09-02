from django.shortcuts import render, redirect
from crm import forms
from crm.models import Employee


# Create your views here.

def employee_add(request):
    form = forms.EmployeeForm()
    context = {"form": form}
    if request.method == "POST":
        form = forms.EmployeeForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            # name = form.cleaned_data['ename']
            # dept = form.cleaned_data['edept']
            # salary = form.cleaned_data['salary']
            # exp = form.cleaned_data['exp']
            # emp = Employee(ename=name, edept=dept, salary=salary, exp=exp)
            # emp.save()
            form.save()
            return redirect("elist")
        else:
            return render(request, 'employee_add.html', context)
    return render(request, 'employee_add.html', context)


def employee_view(request):
    employees = Employee.objects.all()
    context = {}
    context['employees'] = employees
    form = forms.SearchForm()
    context['form'] = form
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['ename']
            employee = Employee.objects.filter(ename__contains=name)
            context['employees'] = employee
            return render(request, 'employee_view.html', context)
    return render(request, 'employee_view.html', context)


def employee_details(request, id):
    employee = Employee.objects.get(id=id)
    context = {}
    context['employee'] = employee
    return render(request, 'employee_details.html', context)


def employee_update(request, id):
    employee = Employee.objects.get(id=id)
    # data = {
    #     "ename": employee.ename,
    #     "edept": employee.edept,
    #     "salary": employee.salary,
    #     "exp": employee.exp
    # }
    form = forms.EmployeeUpdate(instance=employee)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.EmployeeUpdate(request.POST,instance=employee)
        context['form'] = form
        if form.is_valid():
            # name = form.cleaned_data['ename']
            # dept = form.cleaned_data['edept']
            # salary = form.cleaned_data['salary']
            # exp = form.cleaned_data['exp']
            # employee.ename = name
            # employee.edept = dept
            # employee.salary = salary
            # employee.exp = exp
            # employee.save()
            form.save()
            return redirect('elist')
        else:
            return render(request, 'employee_edit.html', context)
    return render(request, 'employee_edit.html', context)


def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('elist')


def login(request):
    form = forms.Login()
    if request.method == 'POST':
        form = forms.Login(request.POST)
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


def register(request):
    form = forms.Register()
    if request.method == 'POST':
        # form = forms.Register(request.POST)
        return redirect('login')
    return render(request, 'register.html', {'form': form})
