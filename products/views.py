from django.shortcuts import render

from .models import Category,Color,Product
from .serializer import CategorySerializer,Colorserializers, ProductCreateSerializers,ProductSerializers
from rest_framework import generics, status,viewsets

class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ColorView(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = Colorserializers

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers

        
        