from django import forms
from .models import RollingStock, Route


class Entry(forms.ModelForm):
    pass


class RsForm(forms.ModelForm):
    start_hour_of_day = forms.TimeField(input_formats='%H:%M', widget=forms.TimeInput(format='%H:%M'))
    num_car = forms.DecimalField()
    start_data = forms.DateField(input_formats='%d.%m.%Y', widget=forms.SelectDateWidget)
    end_data = forms.DateField(input_formats='%d.%m.%Y', widget=forms.SelectDateWidget)
    end_hour_of_day = forms.TimeField(input_formats='%H:%M', widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = RollingStock
        fields = '__all__'


class RouteForm(forms.ModelForm):
    first_car = forms.TimeField(widget=forms.TimeInput(), input_formats='%H:%M')
    last_car = forms.TimeField(widget=forms.TimeInput())

    class Meta:
        model = Route
        fields = '__all__'


