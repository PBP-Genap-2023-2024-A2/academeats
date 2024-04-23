from django.forms import ModelForm, ChoiceField
from makanan.models import Makanan

kategori_choices = (
    ("1", "Camilan"),
    ("2", "Makanan Berat"),
    ("3", "Minuman")
)


class MakananForm(ModelForm):
    kategori = ChoiceField(choices=kategori_choices)

    class Meta:
        model = Makanan
        fields = ['nama', 'deskripsi', 'harga', 'stok', 'img_url']

