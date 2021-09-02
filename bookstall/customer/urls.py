from django.urls import path
from customer import views

urlpatterns = [
    path('signup', views.sign_up, name='signup'),
    path('signin', views.sign_in, name='signin'),
    path('home', views.home, name='home'),
    path('signout', views.signout, name='signout')
]
