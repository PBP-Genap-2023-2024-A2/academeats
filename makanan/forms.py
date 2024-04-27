from django.forms import ModelForm, ChoiceField
from makanan.models import Makanan


class MakananForm(ModelForm):

    class Meta:
        model = Makanan
        fields = ['nama', 'harga', 'stok', 'img_url']
