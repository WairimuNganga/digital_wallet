from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import *
from . import serializer

# Create your views here.
class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class= serializer.Customer_Serializer
