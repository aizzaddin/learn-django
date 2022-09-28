from django.urls import path

from .views import ProductApiView, ProductApiDetailView


urlpatterns = [
    path("product", ProductApiView.as_view(), name="product_list"),
    path("product/<str:pk>", ProductApiDetailView.as_view(), name="product_detail")
]
