from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Society(models.Model):
	name = models.CharField(max_length=50)
	members = models.ManyToManyField(User)
	creation_date = models.DateTimeField(default=timezone.now, editable=False)

	
	def get_members(self):
		return ",\n".join([t.username for t in self.members.all()])
	get_members.short_description = 'Members'


	def __unicode__(self):
		return self.name