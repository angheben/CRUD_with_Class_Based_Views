from django.forms import forms
from .models import Product


class ProductModelForm(forms.BaseForm):
    class Meta:
        model = Product
        fields_ = '__all__'
