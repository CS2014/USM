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


from django.http import HttpResponse
from accounting.models import TransactionCategory, TransactionMethod, Transaction
from accounting.models import Bill, Invoice, Grant, Account
from django.db.models import get_app, get_models
from django.forms.models import model_to_dict
from accounting.models import TransactionCategoryForm, TransactionMethodForm, TransactionForm
from accounting.models import BillForm, InvoiceForm, GrantForm, AccountForm

from main.models import Society
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Displays all the transactions in the list
# Currently not working as intended.

def get_transactions(request,account):
		transaction_list = account.transaction_set.all()
		paginator = Paginator(transaction_list, 5) # Show 25 contacts per page
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

def society_book_keeping(request, slug):
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
		return render(request, 'societies/book-keeping.html', {'account' : account, 
			'transactions':transactions,'form' : transaction_form, 'categories': categories, 'society': society})



'''________________________________________________________________

Below this point are views which are redundant or will be redundant
once the app is complete.

___________________________________________________________________
'''


'''
Index Views:
-Displays a list of existing objects for all socieities with links to more detail and new.

TODO:
Have the returned objects specific to an account which is in the URL.
For example. /DUCSS/accounting/transactions shows the transactions specific 
to DUCCS.
- I played around with this but with no joy.
'''

def index(request):
		app = get_app('accounting')
		app_models = get_models(app)
		context = {'app_models' : app_models}
		return render(request, 'accounting/index.html', context)

def account_index(request):
	account_list = Account.objects.all()
	context = {'account_list': account_list}
	if request.method == 'POST':
		form = AccountForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()    
	return render(request, 'accounts/index.html', context) 

def transaction_category_index(request):
	transaction_category_list = TransactionCategory.objects.all()
	context = {'transaction_category_list': transaction_category_list}
	if request.method == 'POST':
		form = TransactionCategoryForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()    
	return render(request, 'transaction_categories/index.html', context)

def transaction_method_index(request):
	transaction_method_list = TransactionMethod.objects.all()
	context = {'transaction_method_list': transaction_method_list}
	if request.method == 'POST':
		form = TransactionMethodForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()     
	return render(request, 'transaction_methods/index.html', context)

def transaction_index(request):
	transaction_list = Transaction.objects.all()
	context = {'transaction_list': transaction_list}
	if request.method == 'POST':
		form = TransactionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()    
		return HttpResponseRedirect('/')

	return render(request, 'transactions/index.html', context)

def bill_index(request):
	bill_list = Bill.objects.all()
	context = {'bill_list': bill_list}
	if request.method == 'POST':
		form = BillForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()    
	return render(request, 'bills/index.html', context)

def invoice_index(request):
	invoice_list = Invoice.objects.all()
	context = {'invoice_list': invoice_list}
	if request.method == 'POST':
		form = InvoiceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()    
	return render(request, 'invoices/index.html', context)

def grant_index(request):
	grant_list = Grant.objects.all()
	context = {'grant_list': grant_list}
	if request.method == 'POST':
		form = GrantForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()    
	return render(request, 'grants/index.html', context)


'''
Create Views:
- Create and display a form to create a new object.
'''
def account_new(request):
		form = AccountForm
		context = {'form': form}
		return render(request, 'accounts/new.html', context)

def transaction_category_new(request):
		form = TransactionCategoryForm
		context = {'form': form}
		return render(request, 'transaction_categories/new.html', context)

def transaction_method_new(request):
		form = TransactionMethodForm
		context = {'form': form}
		return render(request, 'transaction_methods/new.html', context)

def transaction_new(request):
		form = TransactionForm
		context = {'form': form}
		return render(request, 'transactions/new.html', context)

def bill_new(request):
		form = BillForm
		context = {'form': form}
		return render(request, 'bills/new.html', context)

def invoice_new(request):
		form = InvoiceForm
		context = {'form': form}
		return render(request, 'invoices/new.html', context)

def grant_new(request):
		form = GrantForm
		context = {'form': form}
		return render(request, 'grants/new.html', context)


'''
Detail Views:
- Display the attributes of an object and a form allow for editing.
'''
def account_detail(request, id):
		account = get_object_or_404(Account, pk=id)
		form = AccountForm(data=model_to_dict(account))
		data=build_pretty_data_view(form_instance=form, model_object=account)
		return render(request, 'accounts/detail.html', {'data' : data, 'form' : form})


def transaction_category_detail(request, id):
		transaction_category = get_object_or_404(TransactionCategory, pk=id)
		form = TransactionCategoryForm(data=model_to_dict(transaction_category))
		data=build_pretty_data_view(form_instance=form, model_object=transaction_category)
		return render(request, 'transaction_categories/detail.html', {'data' : data, 'form' : form})

def transaction_method_detail(request, id):
		transaction_method = get_object_or_404(TransactionMethod, pk=id)
		form = TransactionMethodForm(data=model_to_dict(transaction_method))
		data=build_pretty_data_view(form_instance=form, model_object=transaction_method)
		return render(request, 'transaction_methods/detail.html', {'data' : data, 'form' : form})

def transaction_detail(request, id):
		transaction = get_object_or_404(Transaction, pk=id)
		form = TransactionForm(data=model_to_dict(transaction))
		data=build_pretty_data_view(form_instance=form, model_object=transaction)
		return render(request, 'transactions/detail.html', {'data' : data, 'form' : form})

def bill_detail(request, id):
		bill = get_object_or_404(Bill, pk=id)
		form = BillForm(data=model_to_dict(bill))
		data=build_pretty_data_view(form_instance=form, model_object=bill)
		return render(request, 'bills/detail.html', {'data' : data, 'form' : form})

def invoice_detail(request, id):
		invoice = get_object_or_404(Invoice, pk=id)
		form = InvoiceForm(data=model_to_dict(invoice))
		data=build_pretty_data_view(form_instance=form, model_object=invoice)
		return render(request, 'invoices/detail.html', {'data' : data, 'form' : form})

def grant_detail(request, id):
		grant = get_object_or_404(Grant, pk=id)
		form = GrantForm(data=model_to_dict(grant))
		data=build_pretty_data_view(form_instance=form, model_object=grant)
		return render(request, 'grants/detail.html', {'data' : data, 'form' : form})


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
def account_edit(request,id):
	instance = get_object_or_404(Account, id=id)
	form = AccountForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/accounts')
	object = AccountForm(data=model_to_dict(instance))
	return render(request, 'accounts/detail.html', {'object':object})   

def transaction_category_edit(request, id):
	instance = get_object_or_404(TransactionCategory, id=id)
	form = TransactionCategoryForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transaction_categories')
	object = TransactionCategoryForm(data=model_to_dict(instance))
	return render(request, 'transaction_categories/detail.html', {'object':object})  

def transaction_method_edit(request, id):
	instance = get_object_or_404(TransactionMethod, id=id)
	form = TransactionMethodForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transaction_methods')
	object = TransactionMethodForm(data=model_to_dict(instance))
	return render(request, 'transaction_methods/detail.html', {'object':object})    

def transaction_edit(request, id):
	instance = get_object_or_404(Transaction, id=id)
	form = TransactionForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transactions')
	object = TransactionForm(data=model_to_dict(instance))
	return render(request, 'transactions/detail.html', {'object':object})    

def bill_edit(request, id):
	data = {}
	data["username"] = request.user.username
	data["email"] = request.user.email
	return HttpResponse(json.dumps(data), content_type="application/json")

def invoice_edit(request, id):
	instance = get_object_or_404(Invoice, id=id)
	form = InvoiceForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/invoices')
	object = InvoiceForm(data=model_to_dict(instance))
	return render(request, 'invoices/detail.html', {'object':object})    

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
def transaction_category_delete(request, id):
	instance = get_object_or_404(TransactionCategory, id=id)
	form = TransactionCategoryForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transaction_categories')
	object = TransactionCategoryForm(data=model_to_dict(instance))
	return render(request, 'transaction_categories/detail.html', {'object':object})  

def transaction_method_delete(request, id):
	instance = get_object_or_404(TransactionMethod, id=id)
	form = TransactionMethodForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/transaction_methods')
	object = TransactionMethodForm(data=model_to_dict(instance))
	return render(request, 'transaction_methods/detail.html', {'object':object})    

def transaction_delete(request, slug, id):
	Transaction.objects.filter(id=id).delete()
	return redirect('/' +slug+'/transactions/')   

def bill_delete(request, id):
	instance = get_object_or_404(Bill, id=id)
	form = BillForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/bills')
	object = BillForm(data=model_to_dict(instance))
	return render(request, 'bills/detail.html', {'object':object})    

def invoice_delete(request, id):
	instance = get_object_or_404(Invoice, id=id)
	form = InvoiceForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/invoices')
	object = InvoiceForm(data=model_to_dict(instance))
	return render(request, 'invoices/detail.html', {'object':object})    

def grant_delete(request, id):
	instance = get_object_or_404(Grant, id=id)
	form = GrantForm(request.POST or none, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/accounting/grants')
	object = GrantForm(data=model_to_dict(instance))
	return render(request, 'grants/detail.html', {'object':object})
