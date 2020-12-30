from django.conf.urls import url, include
from rest_framework import routers
from .views import *

urlpatterns = [
    url(r'^invoice/$', InvoiceListViewSet.as_view()),
    url(r'^invoice/(?P<pk>\d+)/$', InvoiceViewSet.as_view()),
    url(r'^menu/$', MenuListViewSet.as_view()),
    url(r'^menu/(?P<pk>\d+)/$', MenuViewSet.as_view()),
    url(r'^bahan/$', BahanListViewSet.as_view()),
    url(r'^bahan/(?P<pk>\d+)/$', BahanViewSet.as_view()),
    url(r'^menu-nested/$', MenuNestedViewSet.as_view()),
    # add per week or per month
    url(r'^invoice-nested/$', InvoiceNestedViewSet.as_view()),
]
