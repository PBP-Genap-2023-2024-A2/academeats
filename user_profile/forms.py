from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from user_profile.models import UserProfile


class DaftarForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'nomor_hp',
            'role'
        )
