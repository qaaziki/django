from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product", "is_active", "description", "sale", "price", "image"]