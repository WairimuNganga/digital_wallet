from django.shortcuts import render,redirect
from . import forms
from . import  models
import wallet 

# Create your views here.
#Contents of a HTTP request
def register_customer(request):
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

#Routes-They determine which function is to be followed
def register_card(request):
    if request.method == "POST":
        form = forms.CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})

def register_thirdparty(request):
    if request.method == "POST":
        form = forms.ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ThirPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form})

def register_wallet(request):
    if request.method == "POST":
        form = forms.WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})

def register_currency(request):
    if request.method == "POST":
        form = forms.CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})

def register_receipt(request):
    if request.method == "POST":
        form = forms.ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})

def register_loan(request):
    if request.method == "POST":
        form = forms.LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = forms.LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})

def register_transaction(request):
    if request.method == "POST":
        form = forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})

def register_account(request):
    if request.method == "POST":
        form = forms.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})

def register_reward(request):
    if request.method == "POST":
        form = forms.RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})

def register_notification(request):
    if request.method == "POST":
        form = forms.NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.NotificationRegistrationForm()
    return render(request,"wallet/register_notifications.html",{"form":form})

def list_customers(request):
    customers = models.Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customers})

def list_wallets(request):
    wallets = models.Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",{"wallets":wallets})

def list_cards(request):
    cards = models.Card.objects.all()
    return render(request,"wallet/cards_list.html",{"cards":cards})

def list_thirdparties(request):
    thirdparties = models.ThirdParty.objects.all()
    return render(request,"wallet/thirdparties_list.html",{"thirdparties":thirdparties})

def list_receipts(request):
    receipts = models.Receipt.objects.all()
    return render(request,"wallet/receipts_list.html",{"receipts":receipts})

def list_loans(request):
    loans = models.Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"loans":loans})

def list_transactions(request):
    transactions = models.Transaction.objects.all()
    return render(request,"wallet/transactions_list.html",{"transactions":transactions})

def list_accounts(request):
    accounts = models.Account.objects.all()
    return render(request,"wallet/accounts_list.html",{"accounts":accounts})

def list_rewards(request):
    rewards = models.Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"rewards":rewards})

def list_notifications(request):
    notifications = models.Notification.objects.all()
    return render(request,"wallet/notifications_list.html",{"notifications":notifications})

def list_currencies(request):
    currencies = models.Currency.objects.all()
    return render(request,"wallet/currencies_list.html",{"currencies":currencies})

# Rendering single objects
def customer_profile(request,id):
    customer = models.Customer.objects.get(id=id) 
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_customer(request,id):
    customer= models.Customer.objects.get(id=id)
    if request.method=="POST":
        form = forms.CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
        form = forms.CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_customer.html",{"form":form})

def account_profile(request,id):
    account = models.Account.objects.get(id=id) 
    return render(request,"wallet/account_profile.html",{"account":account})

def edit_account(request,id):
    account= models.Account.objects.get(id=id)
    if request.method=="POST":
        form = forms.AccountRegistrationForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
        form = forms.AccountRegistrationForm(instance=account)
        return render(request,"wallet/edit_account.html",{"form":form})

def wallet_profile(request,id):
    wallet = models.Wallet.objects.get(id=id) 
    return render(request,"wallet/wallet_profile.html",{"wallet":wallet})

def edit_wallet(request,id):
    wallet = models.Wallet.objects.get(id=id)
    if request.method=="POST":
        form = forms.WalletRegistrationForm(request.POST,instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile",id=wallet.id)
    else:
        form = forms.WalletRegistrationForm(instance=wallet)
        return render(request,"wallet/edit_wallet.html",{"form":form})


def card_profile(request,id):
    card = models.Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",{"card":card})

def edit_card(request,id):
    card = models.Wallet.objects.get(id=id)
    if request.method == "POST":
        form = forms.CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id = card.id)   
    else:
        form=forms.CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)

def transaction_profile(request,id):
    transaction = models.Transaction.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",{"transaction":transaction})

def edit_transaction(request,id):
    transaction = models.Transaction.objects.get(id=id)
    if request.method == "POST":
        form = forms.TransactionRegistrationForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id = transaction.id)   
    else:
        form=forms.TransactionRegistrationForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)

def receipt_profile(request,id):
    receipt = models.Receipt.objects.get(id=id)
    return render(request,"wallet/receipt_profile.html",{"receipt":receipt})

def edit_receipt(request,id):
    receipt = models.Receipt.objects.get(id=id)
    if request.method == "POST":
        form = forms.ReceiptRegistrationForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id = receipt.id)   
    else:
        form=forms.ReceiptRegistrationForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=receipt.id)

