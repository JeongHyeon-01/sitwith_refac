from django.urls import path
from .views import SignupView,SigninView,HelloView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('signin/', SigninView.as_view()),
    path('hello/', HelloView.as_view())
]