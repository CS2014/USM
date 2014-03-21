'''
		author: Kevin O'Flanagan
			Cian McDonnell
		date:   2014/march/5


		TODO:
		-Implement views

'''

from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from utils import build_pretty_data_view

from societymembers.models import Tag, SocietyMember, MembershipFee
from django.db.models import get_app, get_models
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from societymembers.models import TagForm, SocietyMemberForm, MembershipFeeForm, DeleteSocietyMemberForm

def member_index(request):
		member_list = SocietyMember.objects.all()
		context = {'member_list' : member_list}
		if request.method == 'POST':
			form = SocietyMemberForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
		return render(request, 'societymembers/index.html', context)

def member_add(request):
		form = SocietyMemberForm
		context = {'form': form}
		return render(request, 'societymembers/new.html', context)

def member_delete(request):
		member_toDelete = get_object_or_404(SocietyMember, pk=request.POST['member_id'])
		user = request.user
		allowed = 0
		for x in member_toDelete.society.members.all():
			if x == user:
				allowed = 1
		if request.method == 'POST':
			if (allowed == 1 or user.is_superuser):
				form = DeleteSocietyMemberForm(request.POST, instance=member_toDelete)
				if form.is_valid():
					member_toDelete.delete()
					return HttpResponseRedirect(reverse('societymembers:member_index'))
			else:
				form = SocietyMemberForm(instance=member_toDelete)
				return HttpResponseRedirect(reverse('societymembers:member_denied'))
		else:
			form = SocietyMemberForm(instance=member_toDelete)

		context = {'form': form}
		return HttpResponseRedirect(reverse('societymembers:member_index'))

def member_edit(request, member_id):
		instance = get_object_or_404(SocietyMember, id=member_id)
		user = request.user
		allowed = 0
		for x in instance.society.members.all():
			if x == user:
				allowed = 1
		if (allowed == 1 or user.is_superuser):
			form = SocietyMemberForm(request.POST or none, instance=instance)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('societymembers:member_index'))
		else:
			return HttpResponseRedirect(reverse('societymembers:member_denied'))
		object = SocietyMemberForm(data=model_to_dict(instance))
		return render(request, 'societymembers/detail.html', {'object':object, 'member_id' : member_id})  

def member_detail(request, member_id):
		member = get_object_or_404(SocietyMember, pk=member_id)
		form = SocietyMemberForm(data=model_to_dict(member))
		data=build_pretty_data_view(form_instance=form, model_object=member)
		return render(request, 'societymembers/detail.html', {'data' : data, 'form' : form, 'member_id' : member_id})

def member_denied(request):
		return render(request, 'societymembers/denied.html')