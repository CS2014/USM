'''
		author: Ross Kinsella
		date:   2014/feb/13

		The first nesting of the URL paths.
		Currently the user selects | creates a society at this point.
'''

from django import forms
from main.forms import UserCreateForm
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
			user_form = UserCreateForm(request.POST)
			if user_form.is_valid():
					print("tet")
					username = user_form.clean_username()
					password = user_form.clean_password2()
					user_form.save()
					return redirect("/")
			else:
				return render(request,
									'main/signup.html',
									{ 'form' : user_form })
		return render(request,
							'main/signup.html')						

def signup_old(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreateForm()
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
