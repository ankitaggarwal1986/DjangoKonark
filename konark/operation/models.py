from django.db import models

# Create your models here.
class Party(models.Model):
    Gstn = models.CharField(max_length=20, null=False, blank=False)
    Name = models.CharField(max_length=20, null=False, blank=False)
    Address= models.CharField(max_length=500)
    PhoneNumber = models.CharField(max_length=50)
    IsSupplier = models.BooleanField()

    def __str__(self):
        return self.Name

class Product(models.Model):
    Hsnid=models.IntegerField(primary_key=True)
    ProductName=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Rate=models.DecimalField(max_digits=6, decimal_places=2)
            
    def __str__(self):
        return self.ProductName

class Tax(models.Model):
    HsnCode=models.IntegerField(primary_key=True)
    Tax=models.DecimalField(max_digits=4, decimal_places=2)

    def __int__(self):
        return self.HsnCode

class Transection(models.Model):
    PartyId=models.IntegerField()
    Quantity=models.IntegerField()
    Date=models.DateField()
    ProductId=models.IntegerField()
    Type=models.TextField()

    def __int__(self):
        return self.PartyId


