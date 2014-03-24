'''
	author: Ross Kinsella
	date:   2014/feb/11
'''

from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Society(models.Model):
	'''
	A master class which Accounts, Communication classes,
	Meetings, Minutes and Society members belong to.
	'''
	name = models.CharField(max_length=50)
	members = models.ManyToManyField(User)
	member_requests = models.ManyToManyField(User,related_name='join_requests')
	creation_date = models.DateTimeField(default=timezone.now, editable=False)
	slug = AutoSlugField('slug', populate_from='name', unique=True)

	def get_members(self):
		return ",\n".join([t.username for t in self.members.all()])
	get_members.short_description = 'Members'

	def __unicode__(self):
		return self.name

class SocietyForm(ModelForm):
	class Meta:
		model = Society
		fields = [ 'name' ]