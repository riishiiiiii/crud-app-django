from django import forms

class CreateForm(forms.Form):
    employee_id = forms.IntegerField()
    name = forms.CharField()
    age = forms.IntegerField()
    number = forms.IntegerField()
