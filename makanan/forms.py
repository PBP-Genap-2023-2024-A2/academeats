from django.forms import ModelForm
from makanan.models import Makanan


class MakananForm(ModelForm):
    class Meta:
        model = Makanan
        fields = ['nama', 'deskripsi', 'harga', 'stok', 'kategori']
