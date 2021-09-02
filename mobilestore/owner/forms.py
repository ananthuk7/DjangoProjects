from django import forms
from django.forms import ModelForm
from owner.models import Mobiles


class MobileAddForm(forms.ModelForm):
    # mobile_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # stock = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Mobiles
        fields = '__all__'
        widgets = {
            'mobile_name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'mobile_name': 'Mobile Name',
        }

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data['price']
        stock = cleaned_data['stock']
        if price < 0:
            msg = 'invalid price'
            self.add_error('price', msg)
        if stock < 0:
            msg = 'enter a valid stock'
            self.add_error('stock', msg)


class MobileUpdateForm(forms.ModelForm):
    # mobile_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # stock = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Mobiles
        fields = '__all__'
        widgets = {
            'mobile_name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'mobile_name': 'Mobile Name',
        }


class SearchForm(forms.Form):
    mobile_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        print('validate')
