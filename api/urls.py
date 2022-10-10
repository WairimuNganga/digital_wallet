from django.urls  import path,include
from . import views
from rest_framework import routers

# Wallet
# Account
# Card
# Transaction
# Loan
# Receipt
# Notification
router = routers.DefaultRouter()
router.register(r"customers",views.CustomerViewSets)
router.register(r"wallets",views.WalletViewSets)
router.register(r"accounts",views.AccountViewSets)
router.register(r"cards",views.CardViewSets)
router.register(r"transactions",views.TransactionViewSets)
router.register(r"loans",views.LoanViewSets)
router.register(r"receipts",views.ReceiptViewSets)
router.register(r"notifications",views.NotificationViewSets)

urlpatterns = [path("",include(router.urls)),]