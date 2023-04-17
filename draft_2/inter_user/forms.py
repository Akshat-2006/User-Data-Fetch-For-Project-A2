from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=10, required=True)
    ref_id = forms.CharField(max_length=20, required=True)
    ver_id = forms.CharField(max_length=8, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.ref_id = self.cleaned_data.get('ref_id')
        user.ver_id = self.cleaned_data.get('ver_id')

        user.save()
        return user