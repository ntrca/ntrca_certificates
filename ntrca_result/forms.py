from django import forms
# from django.forms import formset_factory
# from django.forms import modelformset_factory
from django.forms.models import modelformset_factory
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from .models import NtrcaResult

class NtrcaForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NtrcaForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = NtrcaResult
        fields = ['interview_date', 'board']

        widgets = {
            'interview_date': forms.TextInput(attrs={
                'id': 'interview_date',
                'name':'interview_date',
                'title': 'Enter Your Interview Date',
                'class': 'textfield06a',
                'type': "date",
                'placeholder': 'Enter Your Interview Date'
            }),
            'board': forms.TextInput(attrs={
                'id': 'board',
                'name':'board',
                'title': 'Enter Your Board',
                'class': 'textfield06a',
                'placeholder': 'Enter Your Board'
            })
        }


class NtrcaMarkForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NtrcaMarkForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['s_number'].required = False
        self.fields['v_number'].required = False

    class Meta:
        model = NtrcaResult
        fields = [
            's_number', 'v_number', 'total_number', 'comment'
        ]

        widgets = {
            's_number': forms.NumberInput(attrs={
                'id': 's_number',
                'name': 's_number',
                'title': 'Enter Certificate Number',
                'class': 'textfield06a',
                'placeholder': 'Certificate Mark',
            }),
            'v_number': forms.NumberInput(attrs={
                'id': 'v_number',
                'title': 'Enter Viva Number',
                'name': 'v_number',
                'class': 'textfield06a',
                'placeholder': 'Viva Mark',
            }),
            'total_number': forms.TextInput(attrs={
                'id': 'total_number',
                'title': 'Total Number',
                'class': 'textfield06a',
                'disabled': 'true',
                'placeholder': 'Total Mark'
            }),
            'comment': forms.TextInput(attrs={
                'id': 'comment',
                'title': 'Enter Comment',
                'class': 'textfield06a',
                'placeholder': 'Comment',
            }),
        }
NtrcaMarkFormset = modelformset_factory(NtrcaResult, form=NtrcaMarkForms, extra=0)
