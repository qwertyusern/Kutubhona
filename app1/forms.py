from django import forms
from .models import *

class Studentform(forms.Form):
    ism=forms.CharField(max_length=30)
    guruh = forms.CharField(max_length=30, blank=True)
    bitiruvchi = forms.BooleanField()
    kitoblar_soni =forms.IntegerField()

class Muallifform(forms.Form):
    ism = forms.CharField(max_length=30)
    tirik = forms.BooleanField()
    yosh=forms.IntegerField()
    kitoblar_soni = forms.IntegerField()

class Kitobform(forms.ModelForm):
    class Meta:
        model=kitob
        fields='__all__'
class Recordform(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'