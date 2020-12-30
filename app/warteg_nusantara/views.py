from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class InvoiceListViewSet(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializers


class InvoiceViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializers
    queryset = Invoice.objects.all()


class MenuListViewSet(generics.ListCreateAPIView):
    queryset = MenuWarteg.objects.all()
    serializer_class = MenuWartegSerializers


class MenuViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuWartegSerializers
    queryset = MenuWarteg.objects.all()


class BahanListViewSet(generics.ListCreateAPIView):
    queryset = BahanMenu.objects.all()
    serializer_class = BahanMenuSerializers


class BahanViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BahanMenuSerializers
    queryset = BahanMenu.objects.all()


class MenuNestedViewSet(generics.ListAPIView):
    queryset = MenuWarteg.objects.all()
    serializer_class = MenuWartegNestedSerializers


class InvoiceNestedViewSet(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceNestedSerializers
    """
    for filter base on date per week or per month
    """
