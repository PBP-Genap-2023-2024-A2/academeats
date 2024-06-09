from rest_framework import serializers

from keranjang.models import ItemKeranjang


class KeranjangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemKeranjang
        fields = '__all__'
        depth = 5
