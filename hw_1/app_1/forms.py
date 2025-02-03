from django import forms

class TaskForm(forms.Form):
    a_value = forms.CharField(label='Введите значение числа a:')