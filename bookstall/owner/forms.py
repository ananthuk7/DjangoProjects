from django import forms


class AddBookForm(forms.Form):
    book_name = forms.CharField()
    author_name = forms.CharField()
    price = forms.IntegerField()
    no_of_copies = forms.IntegerField()

    def clean(self):
        print("validation")
