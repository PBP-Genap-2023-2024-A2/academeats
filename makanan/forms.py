from django.forms import ModelForm, ImageField
from makanan.models import Makanan


class MakananForm(ModelForm):
    img_file = ImageField()

    class Meta:
        model = Makanan
        fields = ['nama', 'harga', 'stok']
