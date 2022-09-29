from django.urls import path

from .views import ProductApiView, ProductApiDetailView, ProductApiCreateView, ProductApiUpdateView


urlpatterns = [
    path("product", ProductApiView.as_view(), name="product_list"),
    path("product/<str:pk>", ProductApiDetailView.as_view(), name="product_detail"),
    path("product/add/", ProductApiCreateView.as_view(), name="product_create"),
    path("product/update/<str:pk>", ProductApiUpdateView.as_view(), name="product_update")
]
