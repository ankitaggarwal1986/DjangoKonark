from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('api/party',views.PartyList.as_view()),           #
    path('api/party/<int:pk>', views.PartyDetail.as_view()),
    path('api/product',views.ProductList.as_view()),
    path('api/product/<int:pk>',views.ProductDetail.as_view()),
    path('api/tax',views.TaxList.as_view()),
    path('api/tax/<int:pk>',views.TaxDetail.as_view()),
    path('api/transection',views.TransectionList.as_view()),
    path('api/transection/<int:pk>',views.TransectionDetail.as_view()),
]    