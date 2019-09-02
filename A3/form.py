from django import forms


class dateForm(forms.Form):
    f1 = forms.DateField(label='Desde')
    f2 = forms.DateField(label='Hasta')
