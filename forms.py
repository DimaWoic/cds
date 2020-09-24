from django import forms
from .models import RollingStock


class Entry(forms.ModelForm):
    operation_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = RollingStock
        fields = '__all__'
