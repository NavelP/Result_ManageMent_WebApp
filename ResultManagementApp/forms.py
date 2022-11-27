from django import forms

from .models import *


# model form for the Login
class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['reg_no', 'password']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['reg_no', 'password']


class AddFaculty(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name']


class AddExamEntry(forms.ModelForm):
    class Meta:
        model = ExamEntry
        fields = ['reg_no', 'cat_one', 'cat_two', 'main_exam', 'grade']
