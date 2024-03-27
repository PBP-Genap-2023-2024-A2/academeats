from django import forms

from user_profile.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ("nama",
                  "bio",
                  "role"
                  )
        model = Profile
