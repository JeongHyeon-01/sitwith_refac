import jwt
from django.conf import settings
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from products import serializer
from products.models import Product
from users.models import User

from carts.models import Cart
from utils.decorator import login_authorization,admin_login_authorization
from .serializers import CartSerializers
from utils.permission import CustomReadOnly

class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializers
    
    def get_queryset(self) :

        access_token = self.request.COOKIES['refresh_token']
        payload = jwt.decode(
                access_token,
                settings.SECRET_KEY,
                algorithms=settings.SIMPLE_JWT['ALGORITHM']
            )
        
        user =User.objects.get(id = payload['user_id'])

        return Cart.objects.filter(user_info = user)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CartSerializers(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)


    @login_authorization
    def create(self, request):
        user = request.user.id
        quantity = request.data['quantity']
        cart, state = Cart.objects.get_or_create(
            user_info = User.objects.get(id =user),
            product_info = Product.objects.get(id =int(request.data['product_info'])),
            defaults = {'quantity':0}
        )
        cart.quantity += int(quantity)
        cart.save()

        return Response(status=status.HTTP_201_CREATED)
        