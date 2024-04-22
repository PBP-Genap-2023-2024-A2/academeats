from django.forms import ModelForm
from toko.models import Toko


class TokoForm(ModelForm):
    class Meta:
        model = Toko
        fields = ['name', 'description']
