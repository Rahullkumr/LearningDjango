from django import forms
from .models import StudentModel

"""
class StudentForm(forms.Form):
    sname = forms.CharField(max_length=50)
    srollno = forms.IntegerField()
    course = forms.CharField(max_length=50)
"""


# we can play with the attributes of above class as follows:

# class StudentForm(forms.Form):
#     sname = forms.CharField(max_length=50, min_length=2, label='Student name',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'class': 'snameclass',
#                                     'placeholder': 'enter name'
#                                 }
#                             )
#                             )
#     srollno = forms.IntegerField(initial=22)
#     course = forms.CharField(max_length=50, initial='Django', disabled=True)


# Day 2:
class StudentForm(forms.Form):
    sname = forms.CharField(max_length=50, min_length=2, label='Student name',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'snameclass',
                                    'placeholder': 'enter name'
                                }
                            )
                            )
    srollno = forms.IntegerField(initial=22)
    course = forms.CharField(max_length=50, initial='Django', disabled=True)

    def create(self):
        return StudentModel.objects.create(**self.cleaned_data)

    def update(self, stu):
        stu.sname = self.cleaned_data['sname']
        stu.srollno = self.cleaned_data['srollno']
        stu.course = self.cleaned_data['course']
        stu.save()
