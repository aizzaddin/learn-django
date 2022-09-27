import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    product_name = models.CharField(max_length=200)
    qty = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
