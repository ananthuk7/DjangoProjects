from django import forms
from crm.models import Employee
from django.forms import ModelForm


class EmployeeForm(forms.ModelForm):
    # ename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # edept = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # salary = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # exp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        salary = cleaned_data["salary"]
        exp = cleaned_data["exp"]
        if salary < 0:
            msg = "salary not less than 0"
            self.add_error("salary", msg)
        if exp < 0:
            msg = "experience not greater than 0"
            self.add_error("exp", msg)


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Register(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Confirm_Password = forms.CharField(widget=forms.PassInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(widget=forms.PassInput(attrs={'class': 'form-control'}))


class EmployeeUpdate(forms.ModelForm):
    # ename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # edept = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # salary = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # exp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        salary = cleaned_data["salary"]
        exp = cleaned_data["exp"]
        if salary < 0:
            msg = "salary not less than 0"
            self.add_error("salary", msg)
        if exp < 0:
            msg = "experience not greater than 0"
            self.add_error("exp", msg)


class SearchForm(forms.Form):
    ename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
