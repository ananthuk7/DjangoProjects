from django import forms
from django.forms import ModelForm
from owner.models import Mobiles, Order


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
        mobile = cleaned_data['mobile_name']
        model = cleaned_data['model']
        mobilename = Mobiles.objects.filter(mobile_name=mobile)
        models1 = Mobiles.objects.filter(model=model)
        if mobilename:
            msg = 'already added'
            self.add_error('mobile_name', msg)
        if models1:
            msg = 'invalid model'
            self.add_error('model', msg)
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


class OrderEdit(ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'expected_delivery_date']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'expected_delivery_date': forms.DateInput(attrs={'type':'date'}),

        }
