'''
		author: Ross Kinsella
		date:   2014/feb/13

		The first nesting of the URL paths.
		Currently the user selects | creates a society at this point.
'''

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from main.models import Society
from main.models import SocietyForm
from accounting.models import Account, TransactionForm

def index(request):
		return render(request, 'main/index.html', {})

def signup(request):
		society_list = Society.objects.all()
		form = SocietyForm
		context = {'society_list': society_list, 'form': form}
		return render(request, 'main/signup.html', context)

def create_society(request):
		form = SocietyForm
		if request.method == 'POST':
			form = SocietyForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
			return redirect('/')

def society_page(request, slug):
		society = get_object_or_404(Society, slug=slug)
		return render(request, 'societies/home.html', {'society' : society})

def society_book_keeping(request, slug):
		society = get_object_or_404(Society, slug=slug)
		account = society.account
		transaction_form = TransactionForm(initial={'account': account})
		return render(request, 'societies/book-keeping.html', {'account' : account, 'form' : transaction_form})
