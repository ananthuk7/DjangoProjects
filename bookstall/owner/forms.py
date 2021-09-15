from django import forms
from owner.models import Book, Order
from django.forms import ModelForm


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields=["needed model inputs write here if needed all write __all__"]
        fields = '__all__'
        # fields =['book_name']
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_copies': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'})

        }
        labels = {
            'book_name': 'book name',
            'author_name': 'author',
            'no_of_copies': 'copies'
        }

    # book_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # author_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # no_of_copies = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        book_name = cleaned_data["book_name"]
        price = cleaned_data["price"]
        no_of_copies = cleaned_data["no_of_copies"]
        books = Book.objects.filter(book_name=book_name)
        if books:
            msg = "name already taken"
            self.add_error("book_name", msg)
        if price < 0:
            msg = "enter a valid price"
            self.add_error("price", msg)
        if no_of_copies < 0:
            msg = "enter a valid count"
            self.add_error("no_of_copies", msg)


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_copies': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'})
        }

    # book_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # author_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # no_of_copies = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data["price"]
        no_of_copies = cleaned_data["no_of_copies"]
        if price < 0:
            msg = "enter a valid price"
            self.add_error("price", msg)
        if no_of_copies < 0:
            msg = "enter a valid count"
            self.add_error("no_of_copies", msg)


class SearchForm(forms.Form):
    book_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class ConfirmOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'expected_delivery_date']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'expected_delivery_date': forms.DateInput(attrs={'type': 'date'})
        }
