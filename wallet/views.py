from locale import currency
from django.shortcuts import render
import wallet

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
    form=CustomerRegistrationForm()
    return render(request,"wallet/customer.html",  
    {"cus":form}
      )
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