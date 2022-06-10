from multiprocessing import AuthenticationError
from unicodedata import category
from django.shortcuts import render
from django.db.models import Q

from .models import Category,Color,Product
from .serializer import CategorySerializer,Colorserializers, ProductCreateSerializers,ProductSerializers
from rest_framework import generics, status,filters
from utils.decorator import login_authorization,admin_login_authorization
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend


class CategoryCreatView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   
class ColorCreatView(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = Colorserializers

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers


class ProdcutDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter] 
    filterset_fields = ['category', 'colors','price']
    search_fields = ['$name']
    ordering_fields = ['id','price']
    ordering = ['id']
    permission_classes = [AllowAny]
    
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [AllowAny]
