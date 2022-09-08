from django import forms

class verify_form(forms.Form):
    name = forms.CharField(label='user_name',max_length=100)
    password = forms.CharField(label='password',max_length=100)

class admission_form(verify_form):
    verify_password = forms.CharField(label='verify_password',max_length=100)

class interval_form(forms.Form):
    start_date = forms.DateField(input_formats='%Y-%m-%d %H:%M')
    end_date = forms.DateField(input_formats='%Y-%m-%d %H:%M')

class edit_form(interval_form):
    description = forms.CharField(label='description',max_length=100,required=False)
