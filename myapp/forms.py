from dataclasses import field
from django import forms
from .models import Image,Pdf

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo' : ''}
        
class PdfPage(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = '__all__'
        labels = {'pdf' : ''}