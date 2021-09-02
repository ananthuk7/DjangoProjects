from django.urls import path
from crm import views

urlpatterns = [
    path('employee/', views.employee_view, name="elist"),
    path('employee/add/', views.employee_add, name="add"),
    path('employee/change/<int:id>/', views.employee_update, name="update"),
    path('employee/remove/<int:id>', views.employee_delete, name="remove"),
    path('employee/details/<int:id>', views.employee_details, name="edetails"),
    path('employee/login/', views.login, name="login"),
    path('employee/register/', views.register, name="register")

]
