"""
	author: Ross Kinsella
	date:		2014/2/6

	Models representing the accounting system.
"""

from django.db import models
import datetime
from django.utils import timezone

class Transaction(models.Model):
		''' 
		A single transaction made by a society.
		Can be given a tag to visualise spending by area.

		TODO:
		-method
		-category
		-many to many (log)
		'''

		ammount = models.DecimalField(max_digits=8, decimal_places=2)
		submit_date = models.DateTimeField('submission date')
		bank_reconlliation_date = models.DateTimeField('bank reconcilliation date')
		description = models.CharField(max_length=300)

		def __unicode__(self):
			return self.description

class TransactionCategory(models.Model):
		'''
		A tagging system for transactions to aid in representations.
		Each transaction has a tag summarising the transaction's purpose.

		TODO:
		- Create a forignKey relationship with a transcation.
		'''
		name = models.CharField(max_length=20)
		transaction = models.ForeignKey(Transaction)
		
		def __unicode__(self):
			return self.name


class TransactionMethod(models.Model):
		'''
		A tag descriping how the transaction was conducted;
		eg. was it in cash|cheque

		TODO:
		-have it so that name can only be certain things, eg: cash/cheque.
		-reconsider the description field.
		'''

		transaction = models.ForeignKey(Transaction)
		name = models.CharField(max_length=30)
		description = models.CharField(max_length=300)


class Bill(models.Model):
		'''
		A paid obligation of the society.
		Eg. venue fee.

		TODO:
		-functionality for a recurring bill.
		-many to many (log)

		CONSIDER:
		-adding a transactionCategory?
		'''

		ammount = models.DecimalField(max_digits=8, decimal_places=2)
		description = models.CharField(max_length=300)
		'''
		biller == payee | the receiver of the due ammount
		'''
		biller = models.CharField(max_length=30) 
		creation_date = models.DateTimeField('creation date')
		due_date = models.DateTimeField('due date')

class Invoice(models.Model):
		'''
		An outstanding obligation of the society.
		Eg. accomodation|travel fee. 

		TODO:
		- many to many (log)
		'''

		ammount = models.DecimalField(max_digits=8, decimal_places=2)
		description = models.CharField(max_length=300)
		invoicee = models.CharField(max_length=30)
		creation_date = models.DateTimeField('creation date')
		due_date = models.DateTimeField('due date')

class Grant(models.Model):
		'''
		Money received by the society.
		Eg. Trip grant from Trinity.

		TODO:
		- add a tagging system?
		- add a log relationsip?
		'''

		creation_date = models.DateTimeField('creation date')
		category = models.CharField(max_length=30)
		ammount = models.DecimalField(max_digits=8, decimal_places=2)

class Log(models.Model):
		'''
		Meta data for reviewing changes to enteries over timezone

		TODO:
		- Create the user relationship
		- Have some sort of array of ammounts|dates|users to see changes
			over time to an entry
		'''
		description = models.CharField(max_length=30)
		creation_date = models.DateTimeField('creation date')
		modified_date = models.DateTimeField('modified date')
		ammount = models.DecimalField(max_digits=8, decimal_places=2)