from django.contrib.auth.models import User
from django import forms
from .models import Image, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comments','profile', 'post_date']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['posts', 'followers', 'following', 'user']
        



