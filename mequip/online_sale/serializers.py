from rest_framework import serializers
from online_sale.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user_name', 'first_name', 'last_name', 'address', 'national_code']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'main']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'brand', 'price', 'promotion']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['owner', 'discount_value', 'value', 'final_value']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price', 'discount_price', 'final_price']
