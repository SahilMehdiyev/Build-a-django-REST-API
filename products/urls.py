# from django.urls import path
# from . import views

# urlpatterns = [
#     path('<int:pk>/', views.product_alt_view.as_view(), name='product-detail'),
#     path('',views.product_alt_view.as_view(), name='product-create-list'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductDetailAPIView.as_view(), name='product-list'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    
    path('<int:pk>/', views.ProductListCreateAPIView.as_view(), name='product-create'),
]