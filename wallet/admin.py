from django.contrib import admin


from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email',)
    search_fields=('first_name','last_name')

class CurrencyAdmin(admin.ModelAdmin):
    list_display=('country','symbol','amount')
    search_fields=('country','symbol')

class WalletAdmin(admin.ModelAdmin):
    list_display=('customer','amount','date_created')
    search_fields=('customer','amount')

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_name','account_number','account_balance')
    search_fields=('account_name','account_balance')

class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_number','date')
    search_fields=('receipt_type','receipt_number')

class TransactionAdmin(admin.ModelAdmin):
    list_display=('message','wallet')
    search_fields=('message','wallet','amount','description')

class CardAdmin(admin.ModelAdmin):
    list_display=('expiry_date','wallet','account','issuer')
    search_fields=('wallet','account','issuer')

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=('account','transaction_amount','wallet','issuer')
    search_fields=('transaction_amount','wallet','issuer')

class NotificationAdmin(admin.ModelAdmin):
    list_display=('title','message','date','recipient')
    search_fields=('title','message','date')

class LoanAdmin(admin.ModelAdmin):
    list_display=('wallet','amount')
    search_fields=('message','wallet','amount','description')

class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date_of_reward','points')
    search_fields=('transaction','reciepient','points')


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Reward,RewardAdmin)



