'''
	author: Ross Kinsella
	date:   2014/feb/10

	Adds functionality for creating and editing Society Members, 
	their Tags and their Memership fees.

	TODO:
	- Add society to fields once it has been implemented.
'''

from django.contrib import admin
from societymembers.models import Tag, SocietyMember, MembershipFee

class TagAdmin(admin.ModelAdmin):
	fields = [ 'name', 'society' ]

class SocietyMemberAdmin(admin.ModelAdmin):
	fields = [ 'society', 'name', 'phone_number', 'email_address', 'tags']
	list_display = ('name', 'get_tags')

class MembershipFeeAdmin(admin.ModelAdmin):
	fields = [ 'society_member', 'date_paid', 'expiration_date', 'ammount' ]

admin.site.register(Tag,TagAdmin)
admin.site.register(SocietyMember,SocietyMemberAdmin)
admin.site.register(MembershipFee,MembershipFeeAdmin)