import uuid

from django.db import models
from django.conf import settings


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    product_name = models.CharField(max_length=200)
    qty = models.IntegerField()
    category = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    changed_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
