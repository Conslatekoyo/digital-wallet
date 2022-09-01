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
    path("reward/",register_reward,name="reward")

]