from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "qty",
        "category"
    )


admin.site.register(Product, ProductAdmin)
