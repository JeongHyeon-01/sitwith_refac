from django.urls import path
from .views import CategoryView,ProductCreate,ColorView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('color/',ColorView.as_view()),
    path('product/',ProductCreate.as_view()),
    path('product/<int:product_id>',ProductCreate.as_view())
]
