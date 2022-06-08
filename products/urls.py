from django.urls import path
from .views import CategoryCreatView,ProductCreateView,ColorCreatView,ProductView,ProdcutDetailAdminView

urlpatterns = [
    path('category/', CategoryCreatView.as_view()),
    path('color/',ColorCreatView.as_view()),
    path('create/',ProductCreateView.as_view()),
    path('<int:pk>',ProdcutDetailAdminView.as_view()),
    path('',ProductView.as_view()),
]
