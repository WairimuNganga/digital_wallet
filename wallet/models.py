from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
   first_name = models.CharField(max_length=25,null=True )
   last_name = models.CharField(max_length=25,null=True )
   address = models.TextField(null=True )
   email = models.EmailField(null=True,max_length=50)
   phone_number = models.CharField(max_length=15,null=True )
   gender_choices = (
       ('f','Female'),
       ('m','Male')
   )
   gender = models.CharField(max_length=5,null=True,choices=gender_choices)
   age = models.PositiveSmallIntegerField(null=True)
   password = models.IntegerField(null=True)
   country = models.CharField(max_length=15,null=True)
   id_number = models.IntegerField(null=True)
   profile_picture = models.ImageField(null = True,upload_to = 'profile_picture/')
   date_of_registration = models.DateTimeField(default=timezone.now)
 
class Currency(models.Model):
   country_of_origin = models.CharField(max_length=20,null=True)
   symbol=models.CharField(max_length=5,null=True)
   amount = models.IntegerField(null=True)
 
class Wallet(models.Model):
   balance = models.IntegerField(null=True)
   customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='wallet_customer')
   amount = models.IntegerField(null=True)
   pin = models.TextField(max_length=4,null=True)
   date = models.DateTimeField(default=timezone.now)
   status = models.CharField(max_length=20,null=True)
   currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='wallet_currency')
 
class ThirdParty(models.Model):
   account = models.ForeignKey('Account', on_delete = models.CASCADE,related_name='thirdparty_account')
   name = models.CharField(max_length=20,null=True)
   currency = models.ForeignKey('Currency', on_delete = models.CASCADE,related_name='thirdparty_currency')
   cost = models.IntegerField(null=True)
 
class Receipt(models.Model):
   receipt_type = models.CharField(max_length=30,null=True)
   receipt_date = models.DateField(null=True)
   bill_number = models.IntegerField(null=True)
   transaction = models.OneToOneField('Transaction',on_delete = models.CASCADE,related_name='receipt_transaction')
   receipt_file = models.FileField(upload_to='receipt_file/')
 
class Transaction(models.Model):
   transaction_code = models.CharField(max_length=15,null=True)
   wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE,related_name='transaction_wallet')
   transaction_amount = models.IntegerField(null=True)
   transaction_number = models.IntegerField(null=True)
   transaction_choices = (('withd','withdraw'),('depo','deposit'))
   transaction_type = models.CharField(max_length=10,choices=transaction_choices,null=True)
   transaction_charge = models.IntegerField(null=True)
   transaction_date = models.DateTimeField(default=timezone.now)
   transaction_origin = models.ForeignKey('Account', on_delete = models.CASCADE,related_name='transaction_origin_account')
   transaction_destination = models.ForeignKey('Thirdparty', on_delete = models.CASCADE,related_name='transaction_destination_account')
 
class Account(models.Model):
   account_number = models.IntegerField(null=True)
   accounts = (('f','Fixed'),('c','Current'))
   account_type = models.CharField(max_length=10,null=True,choices=accounts)
   balance = models.IntegerField(null=True)
   wallet = models.ForeignKey('Wallet',on_delete = models.CASCADE,related_name='account_wallet')
 
class Notification(models.Model):
   message = models.CharField(max_length=300,null=True)
   status = (('r','read'),('un','unread'))
   recipient = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='notification_recepient')
   date = models.DateTimeField(default=timezone.now)
   notification_status = models.CharField(max_length=7,choices=status,null=True)
 
class Loan(models.Model):
   loan_ID = models.IntegerField(null=True)
   wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE,related_name='loan_wallet')
   amount = models.IntegerField(null=True)
   loan_term = models.IntegerField(null=True)
   interest_rate = models.IntegerField(null=True)
   loan_balance = models.IntegerField(null=True)
   guarantor = models.ForeignKey('Account', on_delete=models.CASCADE,related_name='loan_guarantor')
   loan_date = models.DateTimeField(default=timezone.now)
   due_date = models.IntegerField(null=True)
 
class Reward(models.Model):
   transaction = models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='reward_transaction')
   date_of_reward = models.DateTimeField(default=timezone.now)
   customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Reward_customer')
   points = models.IntegerField(null=True)
 
class Card(models.Model):
   cardholder_number = models.IntegerField(null=True)
   cardHolder_name = models.CharField(max_length=30,null=True)
   card_status = (('d','debit'),('c','credit'))
   card_type = models.CharField(max_length=5,choices=card_status,null = True)
   expiry_date = models.DateTimeField(default=timezone.now)
   security_code = models.IntegerField(null=True)
   date_issued = models.CharField(max_length=10,null=True)
   wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='card_wallet')
   account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='card_account')
   issuer = models.CharField(max_length=30,null=True)
