from django import forms


class CalculationForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()

    def clean(self):
        print("invalid")


class CubeForm(forms.Form):
    num1 = forms.IntegerField()

    def clean(self):
        print("invalid")
