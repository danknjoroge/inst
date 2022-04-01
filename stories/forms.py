from django.contrib.auth.models import User
from django import forms
from .models import Image

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comments','profile', 'post_date']
        