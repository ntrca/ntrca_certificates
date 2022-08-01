from django import forms
# from django.forms import formset_factory
# from django.forms import modelformset_factory
from django.forms.models import modelformset_factory
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from .models import DuplicateCertificate, DuplicateCertificateFile


class DuplicateCertificateForm(forms.ModelForm):
    """ Duplicate certificate form """
    class Meta:
        model = DuplicateCertificate
        fields = ['note', 'document',]
        # ntrca_certificate
        widgets = {
          'note': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }