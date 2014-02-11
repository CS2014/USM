"""
	author: Ross Kinsella
	date:		2014/2/10

	Models representing the minutes system.
"""
from django.db import models
import datetime
from django.utils import timezone
from accounting.models import Log
from main.models import Society
from societymembers.models import SocietyMember

class Meeting(models.Model):
	'''
	An instance of a meeting.

	TODO:
	- Include the venue?
	- Create a meeting -- society ForeignKey relationship?
	'''
	society = models.ForeignKey(Society)
	society_members = models.ManyToManyField(SocietyMember)

	date = models.DateTimeField()
	title = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.title

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

	def __unicode__(self):
		return self.title


class Minutes(models.Model):
	'''
	The record of a meeting. 
	It may belong to only one meeting.

	TODO:
	- Allow users to import a document as the text?
	'''
	society = models.ForeignKey(Society) 
	attendence = models.ManyToManyField(SocietyMember)

	creation_date = models.DateTimeField(default=timezone.now, editable=False)
	log = models.ManyToManyField(Log)
	text = models.CharField(max_length=10000)
	meeting = models.OneToOneField(Meeting, primary_key = True)

	def __unicode__(self):
		return self.text
