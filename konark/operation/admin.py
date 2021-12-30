from django.contrib import admin
from . models import Party,Product,Tax,Transection
# Register your models here.
MyModels=[Party,Product,Tax,Transection]
admin.site.register(MyModels)
