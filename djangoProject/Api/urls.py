from django.urls import path

from .views import ProductApiView


urlpatterns = [
    path("product", ProductApiView.as_view(), name="book_list")
]
