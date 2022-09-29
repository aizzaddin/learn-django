from django.urls import path
from .views import homePageView, ProductListView


urlpatterns = [
    path("", homePageView, name="home"),
    path("product/", ProductListView.as_view(), name="product")
]