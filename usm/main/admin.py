from django.contrib import admin
from models import Society

class SocietyAdmin(admin.ModelAdmin):
	fields = [ 'name', 'members']
	list_display = [ 'name', 'get_members' ]

admin.site.register(Society,SocietyAdmin)


# Register your models here.
