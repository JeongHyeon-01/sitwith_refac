from .models import Category,Color,Product
from .serializer import CategorySerializer,Colorserializers, ProductCreateSerializers,ProductSerializers
from rest_framework import generics, status,filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from utils.permission import IsLoggedInUserOrAdmin, IsAdminUser, IsAdminUserOrReadOnly

class CategoryCreatView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
   
class ColorCreatView(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = Colorserializers
    permission_classes = [IsAdminUser]
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers
    permission_classes = [IsAdminUser]

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
    
