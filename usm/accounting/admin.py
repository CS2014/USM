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
from accounting.models import Transaction, TransactionMethod, TransactionCategory, Log

class TransactionMethodInLine(admin.TabularInline):
		model = TransactionMethod
		extra = 1

class TransactionCategoryInLine(admin.TabularInline):
		model = TransactionCategory
		extra = 1		

class TransactionAdmin(admin.ModelAdmin):
		fields = [ 'ammount', 'description', 'bank_reconlliation_date' ]
		inlines = [TransactionMethodInLine, TransactionCategoryInLine]
		list_display = ('description', 'ammount', 'get_category', 'get_method','bank_reconlliation_date')

		'''
		Custom definitions to get the tags of the transaction category and method.

		The first element of the TransactionCategory|method object set is retrieved and its
		name field is returned.
		The column is labeled Category|Payment method, as opposed the object's name.
		'''
		def get_category(self,obj):
			return obj.transactioncategory_set.all()[0].name
		get_category.short_description = 'Category'

		def get_method(self,obj):
			return obj.transactionmethod_set.all()[0].name
		get_method.short_description = 'Payment method'

admin.site.register(Transaction, TransactionAdmin)