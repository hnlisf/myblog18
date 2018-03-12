#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import MyPhoto

class PubPhotoForm(forms.ModelForm):
    class Meta:
        model=MyPhoto
        fields=['title','description','photo']