'''
		author: Ross Kinsella
		date:   2014/feb/17


		TODO:
		- Implement redirects when a post request is made 
		   |- To prevent double posting.

		- Have objects specific to a certain account appear.
'''

from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

from accounting.models import TransactionCategory, TransactionMethod, Transaction
from accounting.models import Bill, Invoice, Grant, Account
from django.db.models import get_app, get_models
from django.forms.models import model_to_dict
from accounting.models import TransactionCategoryForm, TransactionMethodForm, TransactionForm
from accounting.models import BillForm, InvoiceForm, GrantForm, AccountForm

# Displays all the transactions in the list
# Currently not working as intended.
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

def transaction_category_index(request, ):
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
- Display the attributes of an object and allow for editing.
'''
def account_detail(request, id):
        form = AccountForm
        account = get_object_or_404(Account, pk=id)
        object = AccountForm(data=model_to_dict(account))
        return render(request, 'accounts/detail.html', {'object' : object})


def transaction_category_detail(request, id):
        form = TransactionCategoryForm
        transaction_category = get_object_or_404(TransactionCategory, pk=id)
        object = TransactionCategoryForm(data=model_to_dict(transaction_category))
        return render(request, 'transaction_categories/detail.html', {'object' : object})

def transaction_method_detail(request, id):
        form = TransactionMethodForm
        transaction_method = get_object_or_404(TransactionMethod, pk=id)
        object = TransactionMethodForm(data=model_to_dict(transaction_method))
        return render(request, 'transaction_methods/detail.html', {'object' : object})

def transaction_detail(request, id):
        form = TransactionForm
        transaction = get_object_or_404(Transaction, pk=id)
        object = TransactionForm(data=model_to_dict(transaction))
        return render(request, 'transactions/detail.html', {'object' : object})

def bill_detail(request, id):
        form = BillForm
        bill = get_object_or_404(Bill, pk=id)
        object = BillForm(data=model_to_dict(bill))
        return render(request, 'bill/detail.html', {'object' : object})

def invoice_detail(request, id):
        form = InvoiceForm
        invoice = get_object_or_404(Invoice, pk=id)
        object = InvoiceForm(data=model_to_dict(invoice))
        return render(request, 'invoices/detail.html', {'object' : object})

def grant_detail(request, id):
        form = GrantForm
        grant = get_object_or_404(Grant, pk=id)
        object = GrantForm(data=model_to_dict(grant))
        return render(request, 'grants/detail.html', {'object' : object})


'''
Edit views:
- Takes a ModelForm, validates and saves it.
- Redirects to relevant index if successful.
- Redirects to detail page if not successful.
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
    instance = get_object_or_404(Bill, id=id)
    form = BillForm(request.POST or none, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounting/bills')
    object = BillForm(data=model_to_dict(instance))
    return render(request, 'bills/detail.html', {'object':object})    

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