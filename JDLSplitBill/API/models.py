import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.CharField(max_length=7)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.domain


class Tagihan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pic_tagihan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nama_resto = models.CharField(max_length=100)
    tanggal_tagihan = models.DateField()
    subtotal = models.IntegerField()
    pajak = models.IntegerField()
    biaya_layanan = models.IntegerField()
    biaya_lainnya = models.IntegerField()
    diskon = models.IntegerField()
    jumlah_total = models.IntegerField()
    created_dt = models.DateTimeField(auto_now_add=True)
    changed_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s' % (self.tanggal_tagihan, self.nama_resto, self.pic_tagihan)


class Pesanan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tagihan = models.ForeignKey(Tagihan, on_delete=models.CASCADE)
    nama_pesanan = models.CharField(max_length=100)
    harga = models.IntegerField()

    def __str__(self):
        return self.nama_pesanan


class Pemesan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tagihan = models.ForeignKey(Tagihan, on_delete=models.CASCADE)
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    qty = models.IntegerField()
    pemesan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.pesanan, self.pemesan, self.qty)


