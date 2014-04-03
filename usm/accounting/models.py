"""
	author: Ross Kinsella
	date:		2014/2/6

	Models representing the accounting system.

	Transaction, Bill and Invoice have a hook save which creteas a Log
	instance whenever they are created / edited.

	TODO: 
	- Have the forms know which society it is.

	- Create functionality for Account.
	   eg. updateBalance()

	- Many of the classes share the same attributes, eg. name | ammount 
	  Is there a way to implement DRY in this respect?

	BUGS:
	- get_logs in bill & invoice returns blank, although the hook save is working.
"""

from django.db import models
from django.forms import ModelForm, Textarea
import datetime
from django.utils import timezone
from main.models import Society
from django.contrib.auth.models import User
from django.db.models import Sum
from django import forms



class Account(models.Model):
	'''
	A holder of all of the above instances for a single Society.

	TODO:
	- Balance field.
	'''
	society = models.OneToOneField(Society)

	def tabulate_transactions_month(self, month):
		today = datetime.date.today()
		x = self.transaction_set.all().filter(submit_date__month=month).aggregate(total=Sum('ammount'))
		if x["total"] != None:
			return x["total"]
		else:
			return 0

	def tabulate_transactions_year(self,month):
		today = datetome.date.today()
		start_month = month

	def tabulate_transactions_jan(self):
		return self.tabulate_transactions_month(1)

	def tabulate_transactions_feb(self):
		return self.tabulate_transactions_month(2)

	def tabulate_transactions_mar(self):
		return self.tabulate_transactions_month(3)

	def tabulate_transactions_apr(self):
		return self.tabulate_transactions_month(4)

	def tabulate_transactions_may(self):
		return self.tabulate_transactions_month(5)

	def tabulate_transactions_jun(self):
		return self.tabulate_transactions_month(6)

	def tabulate_transactions_jul(self):
		return self.tabulate_transactions_month(7)

	def tabulate_transactions_aug(self):
		return self.tabulate_transactions_month(8)

	def tabulate_transactions_sep(self):
		return self.tabulate_transactions_month(9)

	def tabulate_transactions_oct(self):
		return self.tabulate_transactions_month(10)

	def tabulate_transactions_nov(self):
		return self.tabulate_transactions_month(11)

	def tabulate_transactions_dec(self):
		return self.tabulate_transactions_month(12)

  #Get all transaction childrens' ammounts
	def tabulate_transactions(self):
		return self.transaction_set.all().aggregate(total=Sum('ammount'))

	def __unicode__(self):
		return self.society.slug


class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = '__all__'

class Log(models.Model):
		'''
		Meta data for reviewing changes to enteries over timezone

		TODO:
		- Have some sort of array of ammounts|dates|users to see changes
			over time to an entry
		'''

		user = models.ForeignKey(User)

		description = models.CharField(max_length=30)
		creation_date = models.DateTimeField(default=timezone.now, editable=False)

		def __unicode__(self):
			return self.description


class TransactionCategory(models.Model):
		'''
		A tagging system for transactions to aid in representations.
		Each transaction has a tag summarising the transaction's purpose.

		Societies create their own tags.
		'''
		account = models.ForeignKey(Account)	

		name = models.CharField(max_length=20,unique=True)
		
		def __unicode__(self):
			return self.name

class TransactionCategoryForm(ModelForm):
	class Meta:
		model = TransactionCategory
		fields = '__all__'


class TransactionMethod(models.Model):
		'''
		A tag descriping how the transaction was conducted;
		eg. was it in cash|cheque

		Societies create their own tags.

		TODO:
		-reconsider the description field.
		'''

		PAYMENT_CHOICES = ( 
			('Cash', 'cash'),
			('Cheque', 'cheque'),
		)
		account = models.ForeignKey(Account)

		name = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
		description = models.CharField(max_length=300)
		requires_bank_reconciliation = models.BooleanField(default = False)

		def __unicode__(self):
			return self.name

class TransactionMethodForm(ModelForm):
	class Meta:
		model = TransactionMethod
		fields = '__all__'


class Transaction(models.Model):
		''' 
		A single transaction made by a society.
		Can be given a tag to visualise spending by area.

		TODO:
		- Make bank_reconlliation_date manditory if cheque is the payment method.
		'''
		account = models.ForeignKey(Account)
		logs = models.ManyToManyField(Log)
		transaction_category = models.ForeignKey(TransactionCategory)
		transaction_method = models.ForeignKey(TransactionMethod)

		ammount = models.DecimalField(max_digits=8, decimal_places=2)
		submit_date = models.DateTimeField(default=timezone.now, editable=True)
		bank_reconlliation_date = models.DateTimeField('bank reconcilliation date', blank = True, null = True)
		description = models.CharField(max_length=300)

		def save(self, *args, **kwargs):
			super(Transaction, self).save(*args, **kwargs)
			log = Log.objects.create(user = User(id=1), description="test") 
			log.save																											  

		def get_logs(self):
			return ",\n".join([l.user.username + ": "+ l.description for l in self.logs.all()])
		get_logs.short_description = 'Logs'

		def get_stubbed_time(self):
			return self.submit_date.strftime("%d/%m/%Y")

		def __unicode__(self):
			return self.description

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		exclude = ['logs']


class Bill(models.Model):
		'''
		A paid obligation of the society.
		Eg. venue fee.

		TODO:
		-functionality for a recurring bill.

		CONSIDER:
		-adding a transactionCategory?
		'''
		account = models.ForeignKey(Account)
		logs = models.ManyToManyField(Log)
		ammount = models.DecimalField(max_digits=8, decimal_places=2)
		description = models.CharField(max_length=300)

		'''
		biller == payee | the receiver of the due ammount
		'''
		biller = models.CharField(max_length=30) 
		creation_date = models.DateTimeField('creation date')
		due_date = models.DateTimeField('due date')

		def save(self, *args, **kwargs):
			super(Bill, self).save(*args, **kwargs)
			log = Log.objects.create(user = User(id=1), description="bill test") 
			log.save

		def get_logs(self):	
			return ",\n".join([l.user.username + ": "+ l.description for l in self.logs.all()])
		get_logs.short_description = 'Logs'

		def __unicode__(self):
			return self.description

class BillForm(ModelForm):
	class Meta:
		model = Bill
		exclude = ['logs']


class Invoice(models.Model):
		'''
		An outstanding obligation of the society.
		Eg. accomodation|travel fee. 

		'''
		account = models.ForeignKey(Account)
		logs = models.ManyToManyField(Log)

		ammount = models.DecimalField(max_digits=8, decimal_places=2)
		description = models.CharField(max_length=300)
		invoicee = models.CharField(max_length=30)
		creation_date = models.DateTimeField('creation date')
		due_date = models.DateTimeField('due date')

		def save(self, *args, **kwargs):
			super(Invoice, self).save(*args, **kwargs)
			log = Log.objects.create(user = User(id=1), description="invoice test") 
			log.save

		def get_logs(self):	
			return ",\n".join([l.user.username + ": "+ l.description for l in self.logs.all()])
		get_logs.short_description = 'Logs'

		def __unicode__(self):
			return self.description

class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice
		exclude = ['logs']


class Grant(models.Model):
		'''
		Money received by the society.
		Eg. Trip grant from Trinity.

		TODO:
		- add a tagging system?
		- add a log relationsip?
		'''
		account = models.ForeignKey(Account)

		description = models.CharField(max_length=30)
		creation_date = models.DateTimeField('creation date')
		category = models.CharField(max_length=30)
		ammount = models.DecimalField(max_digits=8, decimal_places=2)

class GrantForm(ModelForm):
	class Meta:
		model = Grant
		fields = '__all__' 