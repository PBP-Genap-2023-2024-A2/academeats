from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from user_profile.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = User

    def email_clean(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exist():
            raise ValidationError("Email already exist!")
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ("nama_lengkap", "nama_panggilan", "bio", "role")
        model = Profile
