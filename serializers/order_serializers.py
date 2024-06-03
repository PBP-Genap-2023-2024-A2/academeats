from rest_framework import serializers

from order.models import Order, OrderGroup


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2


class OrderGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGroup
        fields = '__all__'
        depth = 5
