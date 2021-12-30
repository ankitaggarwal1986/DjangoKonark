from django.db.models import fields
from rest_framework import serializers
from . models import Party,Product,Transection,Tax

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = "__all__"

class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transection
        fields = "__all__"                        