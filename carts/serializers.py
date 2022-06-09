from rest_framework import serializers
from .models import Cart

class CartSerializers(serializers.ModelSerializer):
    user_info    = serializers.StringRelatedField(read_only = True)
    products = serializers.StringRelatedField(read_only=True,source = 'product_info')
    quantity     = serializers.IntegerField()
    total_price  = Cart.total_price 
    single_price = Cart.single_price

    class Meta:
        model = Cart
        fields = ['user_info','product_info','products',"quantity","single_price","total_price"]




        
        
