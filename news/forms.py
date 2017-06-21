from django import forms
from .models import *

class NewclientsForm(forms.ModelForm):

    class Meta:
        model = Newclients
        exclude = [""]