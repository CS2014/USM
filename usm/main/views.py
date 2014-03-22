'''
		author: Ross Kinsella
		date:   2014/feb/13

		The first nesting of the URL paths.
		Currently the user selects | creates a society at this point.
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from main.models import Society
from main.models import SocietyForm
from accounting.models import Account, TransactionForm

def index(request):
		context = RequestContext(request)
		return render(request, 'main/index.html', {'context': context})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form,})

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
