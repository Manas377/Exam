from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from user.models import Student, User
from exam.models import TestSet, Question
from result.models import Answer


class TestSetForm(forms.Form):
    question = forms.CharField(disabled=True, required=False)
    choice_1 = forms.CharField(required=False)
    choice_2 = forms.CharField(required=False)
    choice_3 = forms.CharField(required=False)
    choice_4 = forms.CharField(required=False)
    marks = forms.IntegerField()
    correct_choice = forms.CharField()


class TestAnswerForm(forms.Form):
    question = forms.CharField(required=True)
    answer = forms.CharField(required=False)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        # widgets = {'choice_1': forms.RadioSelect, 'choice_2': forms.RadioSelect, 'choice_3': forms.RadioSelect,
        #            'choice_4': forms.}


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

