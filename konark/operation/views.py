from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework import generics
from . serializers import PartySerializer,  ProductSerializer, TaxSerializer, TransectionSerializer
from . models import Party,Product,Tax,Transection

# Create your views here.

class PartyList(generics.ListCreateAPIView):
    queryset =Party.objects.all()  
    serializer_class = PartySerializer

class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party
    serializer_class = Serializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer    

class TaxList(generics.ListCreateAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

class TaxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax
    serializer_class = TaxSerializer

class TransectionList(generics.ListCreateAPIView):
    queryset = Transection.objects.all()
    serializer_class = TransectionSerializer

class TransectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transection
    serializer_class = TransectionSerializer               