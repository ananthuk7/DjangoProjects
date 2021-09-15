from django.urls import path
from customer import views

urlpatterns = [
    path('signup', views.sign_up, name='signup'),
    path('signin', views.sign_in, name='signin'),
    path('', views.home, name='home'),
    path('signout', views.signout, name='signout'),
    path('order/<int:id>', views.order_view, name='orderview'),
    path('order/details', views.order_details, name='orderdetails'),
    path('order/cancel/<int:id>', views.cancel_order, name='cancelorder'),
    path('books/find', views.find_book, name="findbooks")
]
