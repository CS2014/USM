'''
		author: Kevin O'Flanagan
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

def member_delete(request):
		print(11111111111)
		member_toDelete = get_object_or_404(SocietyMember, pk=request.POST['member_id'])
		print(0)
		if request.method == 'POST':
			print(1)
			form = DeleteSocietyMemberForm(request.POST, instance=member_toDelete)
			if form.is_valid():
				print(2)
				member_toDelete.delete()
				return HttpResponseRedirect(reverse('societymembers:member_index'))
		else:
			form = SocietyMemberForm(instance=member_toDelete)

		context = {'form': form}
		return HttpResponseRedirect(reverse('societymembers:member_index'))
