from django import forms
from base.models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name', 'rollno', 'course']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name ',
                    'class': 'stuname'
                }
            )
        }
