from django import forms
from .models import Document, Guideline

class GuidelineForm(forms.ModelForm):
    class Meta:
        model = Guideline
        fields = ('title', 'content')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')