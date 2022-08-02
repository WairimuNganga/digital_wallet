from django.contrib import admin
from .models import Customer,Currency, Notification,ThirdParty,Transaction,Receipt,Wallet,Account,Loan,Reward,Card
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
   list_display = ('first_name','last_name','age','email',)
   search_fields = ('first_name','last_name',)
 
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(ThirdParty)
admin.site.register(Transaction)
admin.site.register(Receipt)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Card)
admin.site.register(Reward)
admin.site.register(Notification)