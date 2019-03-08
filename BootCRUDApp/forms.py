from .models import GarageSaleModel
from django import forms

class GarageSaleForm(forms.ModelForm):
    class Meta:
        model=GarageSaleModel
        fields= "__all__"
