"""
	author: Ross Kinsella
	date:		2014/2/6

	Models representing the accounting system.

	TODO: 
	- Crate functionality for Account.
	   eg. updateBalance()

	- Many of the classes share the same attributes, eg. name | ammount 
	  Is there a way to implement DRY in this respect?
"""

from django.db import models
import datetime
from django.utils import timezone
from main.models import Society


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
		- Create the user relationship
		- Have some sort of array of ammounts|dates|users to see changes
			over time to an entry
		- Have modified_date update automagically.

		CONSIDER:
		- Why is ammount stored here?
		- The log should store who made/edited an entry?
		'''
		description = models.CharField(max_length=30)
		creation_date = models.DateTimeField(default=timezone.now, editable=False)
		modified_date = models.DateTimeField('modified date')
		ammount = models.DecimalField(max_digits=8, decimal_places=2)

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