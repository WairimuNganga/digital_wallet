from rest_framework import serializers
from wallet.models import *

class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name","age","email","address")

class Wallet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields =("balance","customer","amount","date","status")

class Account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("wallet","balance","account_type")

class Card_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_type","cardHolder_name","cardholder_number","wallet","issuer","expiry_date")

class Transaction_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("transaction_type","transaction_charge","transaction_destination","transaction_amount","transaction_date")

class Loan_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("wallet","amount","loan_term","due_date","guarantor","interest_rate")

class Receipt_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("receipt_type","transaction","bill_number","receipt_date")

class Notification_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("recipient","message","date","notification_status")