
from unicodedata import category
from .models import Category,Color, Product,ProductColor

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Colorserializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields ="__all__"

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','price']

class ProductCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['category','colors','name','price','inventory']

    def create(self, validated_data):
        product = Product.objects.create(
            category = validated_data['category'],
            colors = validated_data['colors'],
            name = validated_data['name'],
            price = validated_data['price'],
            inventory = validated_data['inventory']
        )
        
        ProductColor.objects.create(
            product = product,
            color = Color.objects.get(name=validated_data['colors'])
        )
    
        return product