from http.cookiejar import Cookie
from rest_framework import serializers
from .models import Cart
from products.models import Product
from users.models import User
from products.serializer import ProductSerializers
from users.serializer import UserSerializer

class CartSerializers(serializers.ModelSerializer):
    user_info    = serializers.StringRelatedField(read_only = True)
    quantity = serializers.IntegerField()
    

    class Meta:
        model = Cart
        fields = ['user_info','product_info',"quantity"]




        
        
