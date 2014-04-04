'''
		author: Kevin O'Flanagan
			Cian McDonnell
		date:   2014/march/5
'''

from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from utils import build_pretty_data_view

from societymembers.models import Tag, SocietyMember, MembershipFee
from django.db.models import get_app, get_models
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from societymembers.models import TagForm, SocietyMemberForm, MembershipFeeForm, DeleteSocietyMemberForm

from main.models import *

def member_index(request, slug):
	member_list = SocietyMember.objects.filter(society__slug=slug)
	context = {'member_list' : member_list, 'slug': slug}
	return render(request, 'societymembers/index.html', context)

def member_add(request, slug):
	form = SocietyMemberForm
	if request.method == 'POST':
		form = SocietyMemberForm(request.POST, request.FILES)
		if form.is_valid():
			mem = form.save()
			mem.society = Society.objects.get(slug=slug)
			mem.save()
			return HttpResponseRedirect(reverse('societymembers:member_index', args=[slug]))
	context = {'form': form, 'slug': slug}
	return render(request, 'societymembers/new.html', context)

def member_delete(request, slug, member_id):
		member = get_object_or_404(SocietyMember, pk=member_id)

		# Superusers or society admins can delete society members.
		if request.user.is_superuser or request.user.society_set.filter(slug=slug).exists():
				member.delete()
		return HttpResponseRedirect(reverse('societymembers:member_index', args=[slug]))

def member_edit(request, slug, member_id):
		member = get_object_or_404(SocietyMember, id=member_id)
		# Superusers or society admins can delete society members.
		if request.user.is_superuser or request.user.society_set.filter(slug=slug).exists():
			form = SocietyMemberForm(request.POST or none, instance=instance)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('societymembers:member_index', args=[slug]))
		else:
			return HttpResponseRedirect(reverse('societymembers:member_denied'))
		object = SocietyMemberForm(data=model_to_dict(member))
		return render(request, 'societymembers/detail.html', {'object':object, 'member_id' : member_id})  

def member_detail(request, slug, member_id):
		member = get_object_or_404(SocietyMember, pk=member_id)
		form = SocietyMemberForm(data=model_to_dict(member))
		data=build_pretty_data_view(form_instance=form, model_object=member)
		return render(request, 'societymembers/detail.html', {'data' : data, 'form' : form, 'slug':slug, 'member_id' : member_id})

def member_denied(request, slug):
		return render(request, 'societymembers/denied.html')