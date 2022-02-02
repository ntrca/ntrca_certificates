from django import forms
# from django.forms import formset_factory
# from django.forms import modelformset_factory
from django.forms.models import modelformset_factory
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from .models import NtrcaResult, DuplicateCertificate, DuplicateCertificateFile

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

    class Meta:
        model = NtrcaResult
        fields = ['name', 'father', 'mother', 'roll', 's_number', 'v_number', 'total_number', 'comment']

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
    # def clean_s_number(self):
    #     s_number = self.cleaned_data.get('s_number')
    #     if s_number and s_number <= 12:
    #         raise ValidationError('Minimum 12 required')
    #     return s_number
        
    # def clean_v_number(self):
    #     v_number = self.cleaned_data.get('v_number')
    #     if v_number and v_number <= 8:
    #         raise ValidationError('Minimum 8 required')

    #     return v_number

    # def clean(self):
    #     cleaned_data = super().clean()
    #     s_number = cleaned_data.get('s_number')
    #     v_number = cleaned_data.get('v_number')
    #     if s_number:
    #         if s_number > 12:
    #             self.add_error(
    #                 's_number', "Invalid Number"
    #             )

    #     if v_number:
    #         if v_number > 8:
    #             self.add_error(
    #                 'v_number', "Invalid Number"
    #             )
        
NtrcaMarkFormset = modelformset_factory(NtrcaResult, form=NtrcaMarkForms, extra=0)


class DuplicateCertificateForm(forms.ModelForm):
    """ Duplicate certificate form """
    class Meta:
        model = DuplicateCertificate
        fields = ['note', 'document',]
        # ntrca_certificate
        widgets = {
          'note': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }