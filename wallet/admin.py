from django.contrib import admin
from .models import Customer,Currency, Notification,ThirdParty,Transaction,Receipt,Wallet,Account,Loan,Reward,Card
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
   list_display = ('first_name','last_name','age','email',)
   search_fields = ('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
   list_display = ('customer','currency','amount','balance','date')
   search_fields = ('customer','date')
admin.site.register(Wallet,WalletAdmin)

class CurrencyAdmin(admin.ModelAdmin):
   list_display = ('country_of_origin','symbol','amount')
   search_fields = ('country_of_origin','symbol')
admin.site.register(Currency,CurrencyAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
   list_display = ('name','account','currency','cost')
   search_fields = ('account','name')
admin.site.register(ThirdParty,ThirdPartyAdmin)

class ReceiptAdmin(admin.ModelAdmin):
   list_display = ('receipt_type','bill_number','transaction','receipt_date')
   search_fields = ('receipt-type','transaction','receipt_date')
admin.site.register(Receipt,ReceiptAdmin)

class TransactionAdmin(admin.ModelAdmin):
   list_display = ('transaction_code','wallet','transaction_origin','transaction_destination','transaction_date','transaction_type')
   search_fields = ('transaction_type','transaction_origin','transaction_destination')
admin.site.register(Transaction,TransactionAdmin)

class AccountAdmin(admin.ModelAdmin):
   list_display = ('account_number','accounts','account_type','balance','wallet')
   search_fields = ('wallet','account_number')
admin.site.register(Account,AccountAdmin)

class NotificationAdmin(admin.ModelAdmin):
   list_display = ('recipient','date','notification_status','message')
   search_fields = ('notification_status','receipient')
admin.site.register(Notification,NotificationAdmin)

class LoanAdmin(admin.ModelAdmin):
   list_display = ('wallet','amount','loan_term','loan_date','guarantor','interest_rate')
   search_fields = ('amount','wallet','interest_rate')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
   list_display = ('transaction','date_of_reward','customer','points')
   search_fields = ('customer','transaction','points')
admin.site.register(Reward,RewardAdmin)

class CardAdmin(admin.ModelAdmin):
   list_display = ('cardholder_number','cardHolder_name','card_status','wallet','account','date_issued','expiry_date')
   search_fields = ('cardHolder_name','date_issued','expiry_date')
admin.site.register(Card,CardAdmin)




