from django.forms import ModelForm
from django import forms
from .models import *
from django.db import models 


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = (
            'email',
            'message',
        )