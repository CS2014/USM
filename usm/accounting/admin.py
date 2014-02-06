'''
	author: Ross Kinsella
	date:   2014/feb/6

	Creates a list view of all transactions detailing their ammount, category tag
	and payment method 

	TODO:
	- Make line 27(list_display) work as intended
	- Access the child classes of Transaction for the list_display
	- Create another section to view bills|invoices

'''

from django.contrib import admin
from accounting.models import Transaction, TransactionMethod, TransactionCategory

class TransactionMethodInLine(admin.TabularInline):
		model = TransactionMethod
		extra = 1

class TransactionCategoryInLine(admin.TabularInline):
		model = TransactionCategory
		extra = 1		

class TransactionAdmin(admin.ModelAdmin):
		fields = [ 'ammount', 'description','submit_date', 'bank_reconlliation_date' ]
		inlines = [TransactionMethodInLine,TransactionCategoryInLine]
		list_display = ('description', 'ammount', 'bank_reconlliation_date')

		'''
		Broken code:: TODO.

		def get_category(self,obj):
			return obj.TransactionCategory.all[0].name
		get_category.short_description = 'Category'
		'''

admin.site.register(Transaction, TransactionAdmin)		

# Register your models here.
