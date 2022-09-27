from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Product


def homePageView(request):
    return HttpResponse("Hello, World")


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
