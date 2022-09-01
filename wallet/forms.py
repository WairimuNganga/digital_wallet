
from django import forms
from  .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

#create a class to represent what you want to do
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"

class ThirPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = "__all__"
class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"

class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"

class AccountRegistrationForm(forms.ModelForm):

    class Meta:

        model = Account
        fields = "__all__"

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

# Customer,Currency, Notification,ThirdParty,Transaction,Receipt,Wallet,Account,Loan,Reward,Card
# Following the example we have done in class, for each 
# of the models that you have implemented, create the following;
# Model form
# View to render that form
# URL path to send a request to that view
# Template to render the view via the URL path
# Then push your work to Github.
