'''
	author: Ross Kinsella
	date:   2014/feb/6

	Creates a list view of all transactions detailing their ammount, category tag
	and payment method 

	TODO:
	- Create another section to view bills|invoices
	- Display logs

'''

from django.contrib import admin
from accounting.models import Account, Transaction, TransactionMethod, TransactionCategory
from accounting.models import Log, Bill, Invoice

class LogAdmin(admin.ModelAdmin):
		fields = [ 'user', 'description']

class AccountAdmin(admin.ModelAdmin):
	fields = ['society']
	list_display = ['society', 'tabulate_transactions']

class TransactionCategoryAdmin(admin.ModelAdmin):
		fields = [ 'account', 'name' ]

class TransactionMethodAdmin(admin.ModelAdmin):
		fields = [ 'account', 'name', 'description' ]

class TransactionAdmin(admin.ModelAdmin):
		'''
		Creates a transaction :: bank_reconlliation_date is optional.

		TODO:
		- Have bank_reconlliation_date only appear when cheque payment method is selceted.
		'''
		fields = [ 'ammount', 'account' ,'description', 'transaction_category', 'transaction_method' ,'bank_reconlliation_date']
		list_display = ('description', 'ammount' ,'bank_reconlliation_date', 'transaction_category', 'transaction_method', 'get_logs' )	

class BillAdmin(admin.ModelAdmin):
	fields = [ 'account', 'ammount', 'description', 'biller', 'creation_date' ,'due_date' ]
	list_display = [ 'account', 'ammount', 'description', 'biller', 'creation_date' ,'due_date', 'get_logs' ]

class InvoiceAdmin(admin.ModelAdmin):
	fields = [ 'account', 'ammount' ,'description', 'invoicee', 'creation_date', 'due_date' ]
	list_display = [ 'account', 'ammount' ,'description', 'invoicee', 'creation_date', 'due_date' , 'get_logs']


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionCategory, TransactionCategoryAdmin)
admin.site.register(TransactionMethod, TransactionMethodAdmin)
admin.site.register(Log,LogAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Invoice, InvoiceAdmin)