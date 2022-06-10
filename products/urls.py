from django.urls import path
from .views import CategoryCreatView,ProductCreateView,ColorCreatView,ProductView,ProdcutDetailAdminView,ProductDetailView

urlpatterns = [
    path('category/', CategoryCreatView.as_view()),
    path('color/',ColorCreatView.as_view()),
    path('create/',ProductCreateView.as_view()),
    path('product/',ProdcutDetailAdminView.as_view()),
    path('<int:pk>',ProductDetailView.as_view()),
    path('',ProductView.as_view()),
]
