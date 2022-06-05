
from itertools import product
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
    color = serializers.CharField(source='colors.name', read_only= True)
    category = serializers.CharField(source='category.title',read_only = True)
    class Meta:
        model = Product
        fields = ['category','color','id','name','price','inventory']

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

