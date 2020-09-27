from django import forms
from .models import RollingStock, Route


class Entry(forms.ModelForm):
    pass


class RsForm(forms.ModelForm):
    start_hour_of_day = forms.TimeField(widget=forms.TimeInput)
    num_car = forms.IntegerField()
    start_data = forms.DateField(widget=forms.SelectDateWidget)
    end_data = forms.DateField(widget=forms.SelectDateWidget)
    end_hour_of_day = forms.TimeField(widget=forms.TimeInput)

    class Meta:
        model = RollingStock
        fields = '__all__'


class RouteForm(forms.ModelForm):
    first_car = forms.TimeField(widget=forms.TimeInput())
    last_car = forms.TimeField(widget=forms.TimeInput())

    class Meta:
        model = Route
        fields = '__all__'


