'''
		author: Ross Kinsella
		date:   2014/feb/8


		TODO:
		- Complete the index view
'''

from django.shortcuts import render, get_object_or_404

from accounting.models import Transaction
from django.db.models import get_app, get_models

# Displays all the transactions in the list
# Currently not working as intended.
def index(request):
		app = get_app('accounting')
		app_models = get_models(app)
		context = {'app_models' : app_models}
		#context = {'app' : app}
 		return render(request, 'accounting/index.html', context)

def transaction_index(request):
    latest_transaction_list = Transaction.objects.all()
    context = {'latest_transaction_list': latest_transaction_list}
    return render(request, 'transactions/index.html', context)
