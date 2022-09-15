from locale import currency
from urllib import request
from django.shortcuts import render
import wallet
from wallet import forms
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from . import forms

from wallet.forms import CurrencyRegistration, CustomerRegistrationForm, LoanRegistration
from wallet.forms import WalletRegistration
from wallet.forms import NotificationRegistration
from wallet.forms import LoanRegistration
from wallet.forms import ReceiptRegistration
from wallet.forms import Accountregistration
from wallet.forms import TransactionRegistration
from wallet.forms import CardRegistration
from wallet.forms import ThirdPartyRegistration
from wallet.forms import RewardRegistration





# Create your views here.
def register_customer(request):
  if request.method=="POST":
    form=CustomerRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form=CustomerRegistrationForm()
  return render(request,"wallet/customer.html",{"customer":form})
  # form=CustomerRegistrationForm()

    
def register_wallet(request):
  pochi=WalletRegistration()
  return render(request,"wallet/wallet.html",
  {"wall":pochi}
  )
def register_notification(request):
  notify=NotificationRegistration()
  return render(request,"wallet/notification.html",
  {"alert":notify}
  )
def register_currency(request):
  currencies=CurrencyRegistration()
  return render(request,"wallet/currency.html",
  {"current":currencies}
  )
def register_loan(request):
  loans=LoanRegistration()
  return render(request,"wallet/loan.html",
  {"mkopo":loans}
  )

def register_receipt(request):
  receipts=ReceiptRegistration()
  return render(request,"wallet/receipt.html",
  {"bahasha":receipts}
  )

def register_account(request):
  accounts=Accountregistration()
  return render(request,"wallet/account.html",
  {"accounti":accounts}
  )

def register_transaction(request):
  transactions=TransactionRegistration()
  return render(request,"wallet/transaction.html",
  {"transact":transactions}
  )

def register_card(request):
  cards=CardRegistration()
  return render(request,"wallet/card.html",
  {"card":cards}
  )

def register_thirdparty(request):
  thirdparty=ThirdPartyRegistration()
  return render(request,"wallet/thirdparty.html",
  {"thirdparty":thirdparty}
  ) 

def register_reward(request):
  reward=RewardRegistration()
  return render(request,"wallet/reward.html",
  {"rewards":reward}
  ) 

def list_customers(request):
  customer=Customer.objects.all()
  return render(request,"wallet/customer_list.html",{"Customers":customer})

def list_account(request):
  account= Account.objects.all()
  return render(request,"wallet/account_list.html",{"Accounts":account})

def list_card(request):
  card=Card.objects.all()
  return render(request,"wallet/card_list.html",{"Cards":card})

def list_currency(request):
  currency=Currency.objects.all()
  return render(request,"wallet/currency_list.html",{"Currencies":currency})

def list_loan(request):
  loan=Loan.objects.all()
  return render(request,"wallet/loan_list.html",{"Loans":loan})

def list_notification(request):
  notification=Notification.objects.all()
  return render(request,"wallet/notification_list.html",{"Notifications":notification})

def list_receipt(request):
  receipt=Receipt.objects.all()
  return render(request,"wallet/receipt_list.html",{"Receipts":receipt})

def list_reward(request):
  reward=Reward.objects.all()
  return render(request,"wallet/reward_list.html",{"Rewards":reward})

def list_thirdparty(request):
  thirdparty=ThirdParty.objects.all()
  return render(request,"wallet/thirdparty_list.html",{"Thirdparties":thirdparty})

def list_transaction(request):
  transaction=Transaction.objects.all()
  return render(request,"wallet/transaction_list.html",{"Transactions":transaction})

def list_wallet(request):
  wallet=Wallet.objects.all()
  return render(request,"wallet/wallet_list.html",{"Wallets":wallet})