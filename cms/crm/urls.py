from django.urls import path
from crm import views

urlpatterns = [
    path('employee/', views.employee_view),
    path('employee/add/', views.employee_add),
    path('employee/change/<int:id>/', views.employee_update),
    path('employee/remove/<int:id>', views.employee_delete)

]
