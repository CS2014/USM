"""
	author: Ross Kinsella
	date:		2014/2/6

	Models representing the accounting system.

	BUGS:
	- 
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

	def tabulate_transactions_month(self, start_date, end_date, month):
		return self.transaction_set.all().filter(date__range=[start_date, end_date],
			 		date__month= month).aggregate(total=Sum('amount'))
		

	def tabulate_transactions_past_year_by_month(self):
		end_date = datetime.date.today()
		start_date = datetime.date(end_date.year -1, end_date.month, end_date.day)
		monthly_spending = (
			("Jan", self.tabulate_transactions_month(start_date, end_date, 1)),
			("Feb", self.tabulate_transactions_month(start_date, end_date, 2)),
			("Mar", self.tabulate_transactions_month(start_date, end_date, 3)),
			("Apr", self.tabulate_transactions_month(start_date, end_date, 4)),
			("May", self.tabulate_transactions_month(start_date, end_date, 5)),
			("Jun", self.tabulate_transactions_month(start_date, end_date, 6)),
			("Jul", self.tabulate_transactions_month(start_date, end_date, 7)),
			("Aug", self.tabulate_transactions_month(start_date, end_date, 8)),
			("Sep", self.tabulate_transactions_month(start_date, end_date, 9)),
			("Oct", self.tabulate_transactions_month(start_date, end_date, 10)),
			("Nov", self.tabulate_transactions_month(start_date, end_date, 11)),
			("Dec", self.tabulate_transactions_month(start_date, end_date, 12))
		)
		return monthly_spending

  #Get all transaction childrens' amounts
	def tabulate_transactions(self):
		return self.transaction_set.all().aggregate(total=Sum('amount'))

	def tabulate_grants(self):
		return self.grant_set.all().aggregate(total=Sum('amount'))

	def tabulate_balance(self):
		transactions =  self.transaction_set.all().aggregate(total=Sum('amount'))
		grants = self.grant_set.all().aggregate(total=Sum('amount'))
		return grants['total']-transactions['total']

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
		- Have some sort of array of amounts|dates|users to see changes
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

		name = models.CharField(max_length=20)
		
		def __unicode__(self):
			return self.name

class TransactionCategoryForm(ModelForm):
	class Meta:
		model = TransactionCategory
		fields = '__all__'


class Transaction(models.Model):
		''' 
		A single transaction made by a society.
		Can be given a tag to visualise spending by area.
		'''
		PAYMENT_CHOICES = ( 
			('Cash', 'cash'),
			('Cheque', 'cheque'),
		)		

		account = models.ForeignKey(Account)
		logs = models.ManyToManyField(Log)
		transaction_category = models.ForeignKey(TransactionCategory)

		date = models.DateTimeField(default=timezone.now, editable=True)
		amount = models.DecimalField(max_digits=8, decimal_places=2)
		transaction_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
		bank_reconlliation_date = models.DateTimeField('bank reconcilliation date', blank = True, null = True)
		is_reconciled = models.BooleanField(default=False)
		description = models.CharField(max_length=300)

		def save(self, *args, **kwargs):
			super(Transaction, self).save(*args, **kwargs)
			log = Log.objects.create(user = User(id=1), description="test") 
			log.save																											  

		def get_logs(self):
			return ",\n".join([l.user.username + ": "+ l.description for l in self.logs.all()])
		get_logs.short_description = 'Logs'

		def get_stubbed_time(self):
			return self.date.strftime("%d/%m/%Y")

		def __unicode__(self):
			return self.description

class TransactionForm(ModelForm):
	transaction_category = forms.CharField(max_length=20)

	def save(self):
			transaction_name = self.cleaned_data['transaction_category']
			account = self.cleaned_data['account']
			transaction_category, created = TransactionCategory.objects.get_or_create(name=transaction_name, account=account)
			self.instance.transaction_category = transaction_category

			return super(TransactionForm, self).save()

	class Meta:
		model = Transaction
		exclude = ['logs','is_reconciled','transaction_category']


class Grant(models.Model):
		'''
		Money received by the society.
		Eg. Trip grant from Trinity.
		'''
		account = models.ForeignKey(Account)

		description = models.CharField(max_length=30)
		creation_date = models.DateTimeField('creation date')
		purpose = models.CharField(max_length=30)
		amount = models.DecimalField(max_digits=8, decimal_places=2)

		def get_stubbed_time(self):
			return self.creation_date.strftime("%d/%m/%Y")		

class GrantForm(ModelForm):
	class Meta:
		model = Grant
		fields = '__all__' 