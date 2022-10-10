from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import *
from . import serializer

# Create your views here.
class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class= serializer.Customer_Serializer

class WalletViewSets(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = serializer.Wallet_Serializer

class AccountViewSets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializer.Account_Serializer

class CardViewSets(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = serializer.Card_Serializer

class TransactionViewSets(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = serializer.Transaction_Serializer

class LoanViewSets(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = serializer.Loan_Serializer

class ReceiptViewSets(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = serializer.Receipt_Serilizer

class NotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = serializer.Notification_Serializer