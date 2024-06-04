from rest_framework import serializers

from toko.models import Toko


class TokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toko
        fields = '__all__'
        depth = 5
