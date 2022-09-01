from django.urls import path
from .views import register_customer,register_account,register_card,register_currency,register_loan,register_notification,register_receipt,register_reward,register_thirdparty,register_transaction,register_wallet


urlpatterns= [
    path("customer/",register_customer,name="customer"),
    path("account/",register_account,name="account"),
    path("card/",register_card,name="card"),
    path("currency/",register_currency,name="currency"),
    path("loan/",register_loan,name="loan"),
    path("notification/",register_notification,name="notification"),
    path("receipt/",register_receipt,name="receipt"),
    path("reward/",register_reward,name="reward"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("transaction/",register_transaction,name="transaction"),
    path("wallet/",register_wallet,name="wallet"),

]