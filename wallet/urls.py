from django.urls import path
from . import views

urlpatterns= [
    path("customer/",views.register_customer,name="customer"),
    path("account/",views.register_account,name="account"),
    path("card/",views.register_card,name="card"),
    path("currency/",views.register_currency,name="currency"),
    path("loan/",views.register_loan,name="loan"),
    path("notification/",views.register_notification,name="notification"),
    path("receipt/",views.register_receipt,name="receipt"),
    path("reward/",views.register_reward,name="reward"),
    path("thirdparty/",views.register_thirdparty,name="thirdparty"),
    path("transaction/",views.register_transaction,name="transaction"),
    path("wallet/",views.register_wallet,name="wallet"),
    # Url to different list forms
    path("customers/",views.list_customers,name="customers_list"),
    path("cards/",views.list_cards,name="cards_list"),
    path("thirdparties/",views.list_thirdparties,name="thirdparties_list"),
    path("wallets/",views.list_wallets,name="wallets_list"),
    path("currencies/",views.list_currencies,name="currencies_list"),
    path("receipts/",views.list_receipts,name="receipts_list"),
    path("loans/",views.list_loans,name="loans_list"),
    path("transactions/",views.list_transactions,name="transactions_list"),
    path("accounts/",views.list_accounts,name="accounts_list"),
    path("rewards/",views.list_rewards,name="rewards_lists"),
    path("notifications/",views.list_notifications,name="notifications_list")

]