from urllib import request

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class AddQuestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = ['question_text', 'option_one', 'option_two', 'option_three']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-input'}),
            'option_one': forms.TextInput(attrs={'class': 'form-input'}),
            'option_two': forms.TextInput(attrs={'class': 'form-input'}),
            'option_three': forms.TextInput(attrs={'class': 'form-input'}),
            # 'author': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean_title(self):
        title = self.cleaned_data['question_text']
        if len(title) > 255:
            raise ValidationError('Длина превышает 255 символов')

        return title


# class AddChoiceForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = Choice
#         fields = ['choice_text']
#         widgets = {
#             'choice_text': forms.TextInput(attrs={'class': 'form-input'}),
#         }
#
#     def clean_title(self):
#         title = self.cleaned_data['choice_text']
#         if len(title) > 100:
#             raise ValidationError('Длина превышает 100 символов')
#
#         return title
