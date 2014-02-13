"""
	author: Ross Kinsella
	date:		2014/2/6

	Models representing the accounting system.

	Transaction, Bill and Invoice have a hook save which creteas a Log
	instance whenever they are created / edited.

	TODO: 
	- Crate functionality for Account.
	   eg. updateBalance()

	- Many of the classes share the same attributes, eg. name | ammount 
	  Is there a way to implement DRY in this respect?

	BUGS:
	- get_logs in bill & invoice returns blank, although the hook save is working.
"""

from django.db import models
import datetime
from django.utils import timezone
from main.models import Society
from django.contrib.auth.models import User


class Account(models.Model):
	'''
	A holder of all of the above instances for a single Society.

	TODO:
	- Balance field.
	'''
	society = models.OneToOneField(Society)

	def __unicode__(self):
		return self.society.name

class Log(models.Model):
		'''
		Meta data for reviewing changes to enteries over timezone

		TODO:
		- Have some sort of array of ammounts|dates|users to see changes
			over time to an entry

		NB: 
		-- When I added a user field and auto migrated I got this: --
		The field 'Log.user' does not have a default specified, yet is NOT NULL.
 		? Since you are adding this field, you MUST specify a default
 		? value to use for existing rows. Would you like to:
 		?  1. Quit now, and add a default to the field in models.py
 		?  2. Specify a one-off value to use for existing columns now
 		? Please select a choice: 2
 		? Please enter Python code for your one-off default value.
 		>>> 0
	  + Added field user on accounting.Log
		Created 0002_auto__del_field_log_modified_date__add_field_log_user.py.

		-- Likewise, when I removed ammount, I set it to 0 -- 
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

		TODO:
		- Implement a system to allow only certain, society defined, tags be used.
		'''
		#account = models.ForeignKey(Account)	

		name = models.CharField(max_length=20)
		
		def __unicode__(self):
			return self.name


class TransactionMethod(models.Model):
		'''
		A tag descriping how the transaction was conducted;
		eg. was it in cash|cheque

		TODO:
		-reconsider the description field.
		'''

		PAYMENT_CHOICES = ( 
			('Cash', 'cash') ,
			('Cheque', 'cheque'),
		)
		#account = models.ForeignKey(Account)

		name = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
		description = models.CharField(max_length=300)
		requires_bank_reconciliation = models.BooleanField(default = False)

		def __unicode__(self):
			return self.name


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
		submit_date = models.DateTimeField(default=timezone.now, editable=False)
		bank_reconlliation_date = models.DateTimeField('bank reconcilliation date', blank = True, null = True)
		description = models.CharField(max_length=300)

		def save(self, *args, **kwargs):
			super(Transaction, self).save(*args, **kwargs)
			log = Log.objects.create(user = User(id=1), description="test") 
			log.save																											  

		def get_logs(self):
			return ",\n".join([l.user.username + ": "+ l.description for l in self.logs.all()])
		get_logs.short_description = 'Logs'

		def __unicode__(self):
			return self.description 


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

class Grant(models.Model):
		'''
		Money received by the society.
		Eg. Trip grant from Trinity.

		TODO:
		- add a tagging system?
		- add a log relationsip?
		'''
		account = models.ForeignKey(Account)

		creation_date = models.DateTimeField('creation date')
		category = models.CharField(max_length=30)
		ammount = models.DecimalField(max_digits=8, decimal_places=2)