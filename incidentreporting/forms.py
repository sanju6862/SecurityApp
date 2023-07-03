from django import forms
from incidentreporting.models import Incident

class IncidentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    latitude = forms.CharField(widget=forms.HiddenInput())
    longitude = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Incident
        fields = ['incident_type', 'date', 'time', 'zone','description', 'media_file']

    