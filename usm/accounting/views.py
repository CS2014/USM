'''
		author: Ross Kinsella
		date:   2014/feb/8


		TODO:
		- Implement redirects when a post request is made 
		   |- To prevent double posting.

		- Implement the detail views.
'''

from django.shortcuts import render, get_object_or_404

from accounting.models import TransactionCategory, TransactionMethod, Transaction
from accounting.models import Bill, Invoice, Grant, Account
from django.db.models import get_app, get_models

from accounting.models import TransactionCategoryForm, TransactionMethodForm, TransactionForm
from accounting.models import BillForm, InvoiceForm, GrantForm, AccountForm

# Displays all the transactions in the list
# Currently not working as intended.
'''
Index Views:
-Displays a list of existing objects for all socieities with links to more detail and new.
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
Index Views:
- Create and display a form to create a new object.

TODO:

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



