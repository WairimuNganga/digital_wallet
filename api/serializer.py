from rest_framework import serializers
from wallet.models import *

class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name","age","email","address")

class Wallet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields =("balance","customer",)
# balance = models.IntegerField(null=True)
#    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='wallet_customer')
#    amount = models.IntegerField(null=True)
#    pin = models.CharField(max_length=4,null=True)
#    date = models.DateTimeField(default=timezone.now)
#    status = models.CharField(max_length=20,null=True)
#    currenc