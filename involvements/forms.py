from django import forms
from .models import Involvement

class InvolvementForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Involvement
        fields = ['title', 'date','description', 'action_taken']
