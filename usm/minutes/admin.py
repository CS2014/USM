'''
	author: Ross Kinsella
	date:   2014/feb/10

	Adds functionality for creating and editing Meetings, 
	their Minutes and their Agendas.

	TODO:
'''


from django.contrib import admin
from minutes.models import Meeting, Minutes, Agenda

class MeetingAdmin(admin.ModelAdmin):
	fields = [ 'society', 'society_members' ,'date', 'title' ]

class AgendaAdmin(admin.ModelAdmin):
	fields = [ 'date', 'title', 'content', 'meeting', 'log']

class MinutesAdmin(admin.ModelAdmin):
	fields = [ 'society', 'meeting', 'attendence', 'log', 'text'] 

admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Minutes,MinutesAdmin)
admin.site.register(Agenda,AgendaAdmin)

# Register your models here.
