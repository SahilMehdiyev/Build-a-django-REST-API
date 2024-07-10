from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('',views.ProductCreateAPIView.as_view(), name='product-create'),
]
