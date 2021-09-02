from django.shortcuts import render, redirect
from owner import forms
from owner.models import Book


# Create your views here.


# 8000/books/add
def book_create(request):
    if request.method == 'GET':
        form = forms.AddBookForm()
        context = {'form': form}
        return render(request, "book_add.html", context)
    elif request.method == 'POST':
        form = forms.AddBookForm(request.POST)
        if form.is_valid():
            # request.Post ={"book_name":"aaa"}
            # book_name = form.cleaned_data['book_name']
            # author_name = form.cleaned_data['author_name']
            # price = form.cleaned_data['price']
            # no_of_copies = form.cleaned_data['no_of_copies']
            # category = form.cleaned_data['category']
            # book = Book(book_name=book_name, author_name=author_name, price=price, no_of_copies=no_of_copies,
            #             category=category)
            # book.save()
            form.save()
            return redirect("listbook")

        return render(request, "book_add.html", {'form': form})


# 8000/books
def book_list(request):
    books = Book.objects.all()
    form = forms.SearchForm()
    context = {}
    context['books'] = books
    context['form'] = form
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["book_name"]

            book = Book.objects.filter(book_name__contains=book_name)
            context['books'] = book
            return render(request, 'book_list.html', context)
    return render(request, 'book_list.html', context)


# 8000/books/change/{id}
def book_update(request, id):
    book = Book.objects.get(id=id)
    # data = {
    #     'book_name': book.book_name,
    #     'author_name': book.author_name,
    #     'price': book.price,
    #     'no_of_copies': book.no_of_copies,
    #     'category': book.category
    # }
    form = forms.ChangeForm(instance=book)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.ChangeForm(request.POST, instance=book)
        if form.is_valid():
            # book_name = form.cleaned_data['book_name']
            # author_name = form.cleaned_data['author_name']
            # price = form.cleaned_data['price']
            # no_of_copies = form.cleaned_data['no_of_copies']
            # category = form.cleaned_data['category']
            # book.book_name = book_name
            # book.author_name = author_name
            # book.price = price
            # book.no_of_copies = no_of_copies
            # book.category = category
            # book.save()
            form.save()
            return redirect('listbook')
        else:
            return render(request, 'book_edit.html', {'form': form})
    return render(request, 'book_edit.html', context)


# 8000/books/remove/{id}
def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('listbook')


def login(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        return render(request, "login.html", {'form': form})
    return render(request, "login.html", {'form': form})


def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        # form = forms.RegisterForm(request.POST)
        return redirect('login')
    return render(request, "register.html", {'form': form})


def book_details(request, id):
    books = Book.objects.get(id=id)
    context = {}
    context["books"] = books
    return render(request, 'bookdetails.html', context)
