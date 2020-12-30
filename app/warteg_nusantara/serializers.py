from rest_framework import serializers
from warteg_nusantara.models import Invoice, BahanMenu, MenuWarteg


class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ("id", "order_date", "qty_order",
                  "total_order", "uang_bayar", "kembalian")
    """
    order_date = otomastis timezone now
    qty_order = otomatis jumlah dari menu yang diorder
    total_order = otomatis jumlah dari harga yang diorder
    uang_bayar = input decimal by front end
    kembalian = input decimal  
    """


class BahanMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = BahanMenu
        fields = ("id", "bahan", "qty_bahan", "satuan")
    """
    bahan = input char by front end
    qty_bahan = input int by front end
    satuan = input measurement field by front end
    """


class MenuWartegSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuWarteg
        fields = ("id", "makanan", "deskripsi", "tipe",
                  "harga", "qty_menu")
    """
    makanan = input char by front end
    deskripsi = input char by front end
    tipe = input char by front end
    harga = input int by front end
    qty_menu = input int by front end
    """


class MenuWartegNestedSerializers(serializers.ModelSerializer):
    bahan_menu = BahanMenuSerializers(many=True)

    class Meta:
        model = MenuWarteg
        fields = ("id", "makanan", "deskripsi", "tipe",
                  "harga", "qty_menu", "bahan_menu")


class InvoiceNestedSerializers(serializers.ModelSerializer):
    menu_order = MenuWartegSerializers(many=True)

    class Meta:
        model = Invoice
        fields = ("id", "order_date", "menu_order", "qty_order",
                  "total_order", "uang_bayar", "kembalian")
    """
    order date = otomatis timezone now, 
    menuorder = input by id menu
    qty order = otomatis ngitung base on qty menu order
    total order = otomatis ngitung base on jumlah harga menu order
    uang bayar = input int by front end
    kembalian = otomatis ngitung base on uang bayar - total order  
    """
