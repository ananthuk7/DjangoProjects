from django.urls import path
from customer import views

urlpatterns = [
    path('accounts/signup', views.sign_up, name='signup'),
    path('accounts/signin', views.sign_in, name='signin'),
    path('', views.home, name='home'),
    path('signout', views.sign_out, name='signout'),
    path('order/<int:id>', views.order_form, name='orderview'),
    path('orders', views.order_details, name='orderdetails'),
    path('orders/cancel/<int:id>', views.order_cancel, name="ordercancel"),
    path('findmobile', views.find_mobiles, name="findmobile")
]
