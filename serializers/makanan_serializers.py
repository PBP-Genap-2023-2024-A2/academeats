from rest_framework import serializers

from makanan.models import Makanan


class MakananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Makanan
        fields = '__all__'
        depth = 5
