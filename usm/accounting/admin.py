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
from accounting.models import Account, Transaction, TransactionMethod, TransactionCategory, Log

class TransactionMethodInLine(admin.TabularInline):
		model = TransactionMethod
		extra = 1

class TransactionCategoryInLine(admin.TabularInline):
		model = TransactionCategory
		extra = 1

class TransactionInLine(admin.TabularInline):
		model = Transaction
		extra = 3		

class AccountAdmin(admin.ModelAdmin):
	fields = ['society']

class TransactionAdmin(admin.ModelAdmin):
		'''
		Creates a transaction :: bank_reconlliation_date is optional.

		TODO:
		- Have bank_reconlliation_date only appear when cheque payment method is selceted.
		'''
		fields = [ 'ammount', 'account' ,'description', 'transaction_category', 'transaction_method' ,'bank_reconlliation_date' ]
		list_display = ('description', 'ammount' ,'bank_reconlliation_date', 'transaction_category', 'transaction_method')
		

class TransactionCategoryAdmin(admin.ModelAdmin):
		fields = [ 'name' ]
		inlines = [ TransactionInLine ]

class TransactionMethodAdmin(admin.ModelAdmin):
		fields = [ 'name', 'description' ]
		inlines = [ TransactionInLine ]		

class LogAdmin(admin.ModelAdmin):
		fields = [ 'description', 'modified_date', 'ammount' ]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionCategory, TransactionCategoryAdmin)
admin.site.register(TransactionMethod, TransactionMethodAdmin)
admin.site.register(Log,LogAdmin)
admin.site.register(Account,AccountAdmin)