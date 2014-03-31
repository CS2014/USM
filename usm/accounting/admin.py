'''
	author: Ross Kinsella
	date:   2014/feb/6

	Creates a list view of all transactions detailing their amount, category tag
	and payment method 

	TODO:
	- Create another section to view bills|invoices
	- Display logs

'''

from django.contrib import admin
from accounting.models import Account, Transaction, TransactionCategory, Log

class LogAdmin(admin.ModelAdmin):
		fields = [ 'user', 'description']

class AccountAdmin(admin.ModelAdmin):
	fields = ['society']
	list_display = ['society', 'tabulate_transactions']

class TransactionCategoryAdmin(admin.ModelAdmin):
		fields = [ 'account', 'name' ]

class TransactionAdmin(admin.ModelAdmin):
		'''
		Creates a transaction :: bank_reconlliation_date is optional.

		TODO:
		- Have bank_reconlliation_date only appear when cheque payment method is selceted.
		'''
		fields = [ 'amount', 'account' ,'description', 'transaction_category', 'transaction_method' ,'bank_reconlliation_date', 'submit_date']
		list_display = ('description', 'amount' ,'bank_reconlliation_date', 'transaction_category', 'transaction_method', 'get_logs' )	


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionCategory, TransactionCategoryAdmin)
admin.site.register(Log,LogAdmin)
admin.site.register(Account,AccountAdmin)