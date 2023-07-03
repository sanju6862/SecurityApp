from django import forms
from .models import Item

class FoundItemForm(forms.ModelForm):
    # other_type = forms.CharField(required=False)

    class Meta:
        model = Item
        fields = ['item_type','description', 'media']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['other_type'].widget.attrs['style'] = 'display:none;'
    #     self.fields['item_type'].widget.attrs['onchange'] = 'toggleOtherDescription()'
