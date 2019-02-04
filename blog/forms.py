from django import forms
from django.forms import ModelForm

from .models import (Student,
                     Employee)


class StudentSignupForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Student
        fields = '__all__'
        # fields=['name','mob','email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Optional'}),
            'dob': forms.DateInput(attrs={'class': 'datepicker1'}),

            # 'dob': forms.TextInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # super(StudentSignupForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        # print("Fields:",type(self.fields))
        self.fields['name'].required = False
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': "form-control"}
            ),
            'dob': forms.DateInput(
                attrs={'class': "form-control"}
            ),
            'address': forms.Textarea(
                attrs={'class': "form-control"}
            )
        }

    def clean(self):
        name = self.cleaned_data.get('name', False)
        print("Name:", name)
        if not name.isalpha():
            raise forms.ValidationError("Please enter valid name.")
        return self
