"""
	author: Ross Kinsella
	date:		2014/2/10

	Models representing the communication system.

	TODO: 
	- Validators for source_phone_number and sending_address.
	- A sending time.
	- A send_message|email method. There is a library for it from django.
"""
 	 
from django.db import models
from main.models import Society
from societymembers.models import SocietyMember

class TextMessage(models.Model):
	'''
	A text message to be sent to a list of users.

	The content has a limit of 160 chars, which is the length of an SMS by the 
	Global System for Mobile Communications standards.

	source_phone_number is stored in a char field to allow for white space
	and '-' formating.
	'''
	society = models.ForeignKey(Society)
	recipients = models.ForeignKey(SocietyMember)


	name = models.CharField(max_length=40)
	tag = models.CharField(max_length=30)
	content = models.CharField(max_length=160)
	source_phone_number = models.CharField(max_length=25)

	def __unicode__(self):
		return self.name	

class Email(models.Model):
	'''
	An email to be sent to a list of users.
	'''
	society = models.ForeignKey(Society)
	recipients = models.ForeignKey(SocietyMember)

	name = models.CharField(max_length=40)
	tag = models.CharField(max_length=30)
	content = models.CharField(max_length=160)
	sending_address = models.CharField(max_length=60)
	
	def __unicode__(self):
		return self.name

