
from django import forms
from .models import *
from inventory.models import *

class OrderForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity', min_value=1)

class SellForm(forms.Form):
    quantity_sold = forms.IntegerField(label='quantity_sold', min_value=1)

class TransForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity', min_value=1)