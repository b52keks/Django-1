from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, label='Имя')
    phone = forms.CharField(max_length=200, label='Телефон')