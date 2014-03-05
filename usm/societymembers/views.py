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
from societymembers.models import TagForm, SocietyMemberForm, MembershipFeeForm