from django.shortcuts import render


# Create your views here.

def employee_add(request):
    return render(request, 'employee_add.html')


def employee_view(request):
    return render(request, 'employee_view.html')


def employee_update(request, id):
    return render(request, 'employee_edit.html')


def employee_delete(request, id):
    return render(request, 'employee_delete.html')
