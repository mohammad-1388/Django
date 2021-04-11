from django import forms
from django.contrib.auth.forms import UserChangeForm

from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'idUser', 'profile_picture']
        exclude = ['user']


class MyUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']

    password = None
