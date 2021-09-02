from django import forms
from owner.models import Book
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
            'category':forms.TextInput(attrs={'class': 'form-control'})

        }
        labels={
            'book_name':'book name',
            'author_name':'author',
            'no_of_copies':'copies'
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


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'ename': forms.TextInput(attrs={'class': 'form-control'}),
            'edept': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'exp': forms.NumberInput(attrs={'class': 'form-control'})
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
