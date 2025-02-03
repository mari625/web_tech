from django import forms
from django.forms import ModelForm
from .models import TaskModel


class TaskForm(forms.Form):
    task = forms.CharField(initial="Дано вещественное число A. Вычислить x = a**4, при a < 10; x = a при a > 61, в противном случае x  = a − sin(a**2)).")
    a = forms.FloatField(initial=1)


class TaskModelForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        print('\nfields: ', fields)
