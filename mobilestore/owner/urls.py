from django.urls import path
from owner import views

urlpatterns = [
    path('mobiles/', views.view_mobiles, name="viewmobile"),
    path('mobiles/add/', views.add_mobile, name='addmobile'),
    path('mobiles/remove/<int:id>/', views.remove_item, name='removemobile'),
    path('mobiles/change/<int:id>/', views.update_mobile, name='updatemobile'),
    path('mobiles/details/<int:id>', views.mobile_details, name='mobiledetails'),
    path('mobiles/login', views.login, name='login'),
    path('mobiles/register', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('orderedit/<int:id>', views.order_edit, name='orderedit')

]
