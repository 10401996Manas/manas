from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer