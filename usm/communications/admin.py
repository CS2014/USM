'''
	author: Ross Kinsella
	date:   2014/feb/10

	Adds functionality for creating and editing Communication instances.

	TODO:
'''
from django.contrib import admin
from communications.models import TextMessage, Email

class TextMessageAdmin(admin.ModelAdmin):
	fields = ['name', 'tag', 'content', 'source_phone_number'] 

class EmailAdmin(admin.ModelAdmin):
	fields = ['name', 'tag', 'content', 'sending_address' ]

admin.site.register(TextMessage,TextMessageAdmin)
admin.site.register(Email,EmailAdmin)