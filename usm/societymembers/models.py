"""
	author: Ross Kinsella
	date:		2014/2/10

	Models representing and supporting members of a society.

	TODO: 
	- Implement and import Society.
"""

from django.db import models
import datetime
from django.utils import timezone
from main.models import Society

class Tag(models.Model):
	'''
	A tagging system for easily finding members.
	For example: A 'Goal keeper' tag or 'Django developer' tag.
	'''
	name = models.CharField(max_length=30)
	society = models.ForeignKey(Society)

	def __unicode__(self):
		return self.name	


class SocietyMember(models.Model):
	'''
	A member of a society.

	The phone_number field is stored in a char field to allow for white space
	and '-' formating.
	'''
	tags = models.ManyToManyField(Tag)
	society = models.ForeignKey(Society)

	name = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=25)
	email_address = models.CharField(max_length=60)
	join_date = models.DateTimeField('join date')

	
	'''
	Returns a string of all tags seperated by ','.
	'''
	def get_tags(self):
		return ",\n".join([t.name for t in self.tags.all()])
	get_tags.short_description = 'Tags'

	def __unicode__(self):
		return self.name


class MembershipFee(models.Model):
	'''
	A fee which must be paid by members to be a part of the society.

	TODO:
	- Is valid method. --> returns ( expiration_date < now() )
	'''
	society_member = models.ForeignKey(SocietyMember)

	date_paid = models.DateTimeField('date paid')
	expiration_date = models.DateTimeField('expiration_date')
	ammount = models.DecimalField(max_digits = 4, decimal_places = 2)

	def __unicode__(self):
		return unicode(self.society_member.name)


