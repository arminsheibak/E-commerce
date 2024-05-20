from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "collection",
            "inventory",
            "unit_price",
            "price_with_tax",
            "description",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.StringRelatedField()

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "name", "description", "date", "product"]

    product = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        id = self.context["product_id"]
        return Review.objects.create(product_id=id, **validated_data)
