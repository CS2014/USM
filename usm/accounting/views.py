'''
		author: Ross Kinsella
		date:   2014/feb/17


		TODO:
		- Implement redirects when a post request is made 
		   |- To prevent double posting.

		- Have objects specific to a certain account appear.
'''
import json
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from utils import build_pretty_data_view

from accounting.models import TransactionCategory, Transaction
from accounting.models import Grant, Account

from django.db.models import get_app, get_models
from django.forms.models import model_to_dict
from accounting.models import TransactionCategoryForm, TransactionForm
from accounting.models import  GrantForm, AccountForm
from django.views.decorators.csrf import csrf_exempt

from main.models import Society
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime

# Displays all the transactions in the list
# Currently not working as intended.

def get_transactions(request,account):
		transaction_list = account.transaction_set.all()
		paginator = Paginator(transaction_list, 15) # Show 25 contacts per page
		page = request.GET.get('page')
		try:
				transactions = paginator.page(page)
		except PageNotAnInteger:
		    # If page is not an integer, deliver first page.
				transactions = paginator.page(1)
		except EmptyPage:
		    # If page is out of range (e.g. 9999), deliver last page of results.
				transactions = paginator.page(paginator.num_pages)
		return transactions	

def get_grants(request,account):
		grant_list = account.grant_set.all()
		paginator = Paginator(grant_list, 15) # Show 25 contacts per page
		page = request.GET.get('page')
		try:
				grants = paginator.page(page)
		except PageNotAnInteger:
		    # If page is not an integer, deliver first page.
				grants = paginator.page(1)
		except EmptyPage:
		    # If page is out of range (e.g. 9999), deliver last page of results.
				grants = paginator.page(paginator.num_pages)
		return grants				

def transactions(request, slug):
		society = get_object_or_404(Society, slug=slug)
		try:
			society.members.get(pk=request.user.id)
		except society.DoesNotExist:
			return HttpResponseRedirect('/')

		account = society.account
		transactions = get_transactions(request,account)
		categories = TransactionCategory.objects.filter(account=account)

		if request.method == 'POST':
				form = TransactionForm(request.POST, request.FILES)
				if form.is_valid():
					form.save()
				else:
					print form.errors
				return redirect('/'+slug+'/transactions')
		transaction_form = TransactionForm(initial={'account': account})
		return render(request, 'accounting/transactions.html', {'account' : account, 
			'transactions':transactions,'form' : transaction_form, 'society': society})


def grants(request, slug):
		society = get_object_or_404(Society, slug=slug)
		try:
			society.members.get(pk=request.user.id)
		except society.DoesNotExist:
			return HttpResponseRedirect('/')

		account = society.account
		grants = get_grants(request,account)

		if request.method == 'POST':
				form = GrantForm(request.POST, request.FILES)
				if form.is_valid():
					form.save()
				else:
					print form.errors
				return redirect('/'+slug+'/grants')
		grant_form = GrantForm(initial={'account': account})
		return render(request, 'accounting/grants.html', {'account' : account, 
			'grants':grants,'form' : grant_form, 'society': society})	


def reconcile_transaction(request, slug, id):
		society = get_object_or_404(Society, slug=slug)
		try:
			society.members.get(pk=request.user.id)
		except society.DoesNotExist:
			return HttpResponseRedirect('/')

		account = society.account
		transaction = Transaction.objects.get(id=id)		

		if transaction.is_reconciled == True:
			transaction.is_reconciled = False
			transaction.save()
		else:
			transaction.is_reconciled = True
			transaction.bank_reconlliation_date = datetime.datetime.now()
			transaction.save()
		return redirect('/'+slug+'/transactions')




'''________________________________________________________________

Below this point are views which are redundant or will be redundant
once the app is complete.

___________________________________________________________________
'''


'''
Edit views:
- Takes a ModelForm, validates and saves it.
- Redirects to relevant index if successful.
- Redirects to detail page if not successful.

BUGS:
- If you edit the society which an account represents,
  It keeps the transactions.
  However, changing the society it belongs to is not logical
  so the real bug is that you can change the society.
'''

def transaction_category_edit(request, id):
	instance = get_object_or_404(TransactionCategory, id=id)
	form = TransactionCategoryForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transaction_categories')
	object = TransactionCategoryForm(data=model_to_dict(instance))
	return render(request, 'transaction_categories/detail.html', {'object':object})   

def transaction_edit(request, id):
	instance = get_object_or_404(Transaction, id=id)
	form = TransactionForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transactions')
	object = TransactionForm(data=model_to_dict(instance))
	return render(request, 'transactions/detail.html', {'object':object})       

def grant_edit(request, id):
	instance = get_object_or_404(Grant, id=id)
	form = GrantForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/grants')
	object = GrantForm(data=model_to_dict(instance))
	return render(request, 'grants/detail.html', {'object':object})      

'''
Delete views:
'''  
def transaction_category_delete(request, slug, id):
	Transaction.objects.filter(id=id).delete()
	return redirect('/' +slug+'/transactions/')   

def transaction_delete(request, slug, id):
	Transaction.objects.filter(id=id).delete()
	return redirect('/' +slug+'/transactions/')   

def grant_delete(request, slug, id):
	Grant.objects.filter(id=id).delete()
	return redirect('/' +slug+'/grants/')
