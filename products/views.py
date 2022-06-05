from unicodedata import category
from django.shortcuts import render
from django.db.models import Q

from .models import Category,Color,Product
from .serializer import CategorySerializer,Colorserializers, ProductCreateSerializers,ProductSerializers
from rest_framework import generics, status,filters
from utils.decorator import login_authorization,admin_login_authorization

from django_filters.rest_framework import DjangoFilterBackend


class CategoryCreatView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = admin_login_authorization    

class ColorCreatView(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = Colorserializers
    permission_classes= admin_login_authorization

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers
    permission_classes = admin_login_authorization

class ProdcutDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers
    permission_classes =admin_login_authorization

   
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter] 
    filterset_fields = ['category', 'colors','price']
    search_fields = ['$name']
    ordering_fields = ['id','price']
    ordering = ['id']
    
class ProdcutDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
