# from tkinter import N
from django.urls import path
from .views import register_currency, register_customer, register_loan, register_reward, register_thirdparty
from .views import register_wallet
from .views import register_notification
from .views import register_loan
from .views import register_receipt
from .views import register_account
from .views import register_transaction
from .views import register_card
from .views import register_thirdparty
from .views import register_reward
from . import views


urlpatterns=[
    path("register/",register_customer, name="registration"),
    path("wallets/",register_wallet, name = "diffwallets"),
    path("notify/",register_notification,name="alerts"),
    path("currencies/",register_currency,name="current"),
    path("loan/",register_loan,name="loans"),
    path("receipt/",register_receipt,name="receipts"),
    path("account/",register_account,name="accounts"),
    path("transaction/",register_transaction,name="transactions"),
    path("card/",register_card,name="cards"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("reward/",register_reward,name="reward"),
    path("customers/",views.list_customers, name="list"),
    path("accounts/",views.list_account, name="acc"),
    path("cards/",views.list_card, name="car"),
    path("currencies/",views.list_currency, name="curr"),
    path("loans/",views.list_loan, name="loa"),
    path("notifications/",views.list_notification, name="notifi"),
    path("receipts/",views.list_receipt, name="rece"),
    path("rewards/",views.list_reward, name="rew"),
    path("thirdparties/",views.list_thirdparty, name="third"),
    path("transactions/",views.list_transaction, name="transact"),
    path("wallets/",views.list_wallet, name="wallet")













]