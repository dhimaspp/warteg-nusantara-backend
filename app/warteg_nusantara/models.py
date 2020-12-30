from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    order_date = models.DateTimeField(default=timezone.now)
    qty_order = models.DecimalField(max_digits=5, decimal_places=0)
    total_order = models.DecimalField(max_digits=12, decimal_places=0)
    uang_bayar = models.DecimalField(
        max_digits=12, decimal_places=0, default=0)
    kembalian = models.DecimalField(max_digits=12, decimal_places=0, default=0)


class MenuWarteg(models.Model):
    makanan = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255, blank=True, null=True)
    tipe = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=12, decimal_places=0)
    qty_menu = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    invoices = models.ManyToManyField(
        Invoice, blank=True, related_name="invoices_menu")


class BahanMenu(models.Model):
    bahan = models.CharField(max_length=255)
    qty_bahan = models.DecimalField(max_digits=5, default=0, decimal_places=0)
    satuan = models.DecimalField(max_digits=7, default=0, decimal_places=0)
    menus = models.ManyToManyField(
        MenuWarteg, blank=True, related_name="bahan_menu")
