"""
	author: Ross Kinsella
	date:		2014/2/10

	Models representing the minutes system.

	TODO: 
	- implement and import Society | SocietyMember class.
"""
from django.db import models
import datetime
from django.utils import timezone
from accounting.models import Log

class Meeting(models.Model):
	'''
	An instance of a meeting.

	TODO:
	- Include the venue?
	- Create a meeting -- society ForeignKey relationship?
	'''
	date = models.DateTimeField()
	title = models.CharField(max_length = 100)
	'''
	TODO:
	society_members = models.ManyToManyField(SocieryMember)
	'''

class Agenda(models.Model):
	'''
	The goal of the meeting.

	TODO:
	- Create a topics field?
	'''
	date = models.DateTimeField()
	title = models.CharField(max_length = 100)
	content = models.CharField(max_length = 10000)
	meeting = models.OneToOneField(Meeting, primary_key=True)
	log = models.ManyToManyField(Log)


class Minutes(models.Model):
	'''
	The record of a meeting. 
	It may belong to only one meeting.

	TODO:
	- Allow users to import a document as the text?
	'''
	creation_date = models.DateTimeField(default=timezone.now, editable=False)
	log = models.ManyToManyField(Log)
	text = models.CharField(max_length=10000)
	meeting = models.OneToOneField(Meeting, primary_key = True)
	'''
	TODO:
	society = models.ForeignKey(Society) 
	attendence = models.ManyToManyField(SocietyMember)
	'''

