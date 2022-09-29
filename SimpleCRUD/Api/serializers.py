from rest_framework import serializers

from Supermarket.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "product_name", "category", "qty", "created_by", "created_dt", "changed_dt")
