from django.urls import path
from owner import views

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path('books/add', views.book_create, name="addbook"),
    path('books/', views.book_list, name="listbook"),
    path('books/change/<int:id>/', views.book_update, name="changebook"),
    path('books/remove/<int:id>/', views.book_delete, name="removebook"),
    path('books/bookdetails/<int:id>', views.book_details, name="bookdetails"),
    path('books/orderedit/<int:id>',views.orderedit,name="orderedit"),


]
