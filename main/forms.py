from django import forms
from .models import tag

class DateInput(forms.DateInput):
    input_type = 'date'

class NewEntryForm(forms.Form):
    content = forms.CharField(label = "Content",max_length=500)
    priority = forms.IntegerField(label = "Priority")
    tag = forms.ModelChoiceField(queryset = tag.objects.all(), empty_label="None", required=False)
