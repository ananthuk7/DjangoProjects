from django.shortcuts import render
from owner import forms


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
            book_name = form.cleaned_data['book_name']
            author_name = form.cleaned_data['author_name']
            price = form.cleaned_data['price']
            no_of_copies = form.cleaned_data['no_of_copies']
            print(book_name, author_name, price, no_of_copies)
            return render(request, "book_add.html", {'form': form})

        return render(request, "book_add.html", {'form': form})


# 8000/books
def book_list(request):
    return render(request, 'book_list.html')


# 8000/books/change/{id}
def book_update(request, id):
    # if request.method == 'GET':
    #     form = forms.AddBookForm()
    #     context = {'form': form}
    return render(request, 'book_edit.html')


# 8000/books/remove/{id}
def book_delete(request, id):
    return render(request, 'book_remove.html')
