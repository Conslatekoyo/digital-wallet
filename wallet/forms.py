from dataclasses import field, fields
from pyexpat import model
# from pyexpat import model
from django import forms

from wallet.models import Customer, Notification, Receipt, Reward, ThirdParty, Transaction
from wallet.models import Wallet
from wallet.models import Notification
from wallet.models import Currency
from wallet.models import Loan
from wallet.models import Receipt
from wallet.models import Account
from wallet.models import Transaction
from wallet.models import Card
from wallet.models import ThirdParty
from wallet.models import Reward

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class WalletRegistration(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"

class NotificationRegistration(forms.ModelForm):
    class Meta:
        model=Notification
        fields="__all__"

class CurrencyRegistration(forms.ModelForm):
    class Meta:
        model=Currency
        fields="__all__"

class LoanRegistration(forms.ModelForm):
    class Meta:
        model=Loan
        fields="__all__"

class ReceiptRegistration(forms.ModelForm):
    class Meta:
        model=Receipt
        fields="__all__"

class Accountregistration(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"
class TransactionRegistration(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"

class CardRegistration(forms.ModelForm):
    class Meta:
        model=Card
        fields="__all__"

class ThirdPartyRegistration(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields="__all__"

class RewardRegistration(forms.ModelForm):
    class Meta:
        model=Reward
        fields="__all__"