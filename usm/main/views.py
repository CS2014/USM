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
from django.db.models import get_app, get_models

from main.models import Society
from main.models import SocietyForm
from accounting.models import Account, TransactionForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def homepage(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
    	return user_homepage(request)
    if request.method == 'POST':
    	return log_in(request)
    else:
      return render(request, 'main/index.html', {'context': context})

def user_homepage(request):
    context = RequestContext(request)
    form = SocietyForm
    return render(request, 'main/user_homepage.html', {'context': context, 'form':form})

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return homepage(request)
        else:
            return redirect("/banned_user")
    else:
        messages.add_message(request, messages.INFO, "Your user name and password do not match")
        return redirect("/#log-in")

def signup(request):
		if request.method == 'POST':
			user_form = UserCreateForm(request.POST)
			if user_form.is_valid():
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

def logout_view(request):
		logout(request)
		return redirect('/')

def dash_board(request, slug): 
		society = get_object_or_404(Society, slug=slug)
		if society.members.get(pk=request.user.id):
			return render(request, 'accounting/index.html', {'society': society})
		else:
			return redirect('no_permission')

def request_membership(request):
		if request.method == 'POST':
			slug = request.POST['slug']
			society = get_object_or_404(Society, slug=slug)
			society.member_requests.add(request.user)
			messages.add_message(request, messages.INFO, "Your request has been sent. You will be notified when it is accepted.")
		return redirect('/')

def member_requests(request,slug):
		society = get_object_or_404(Society, slug=slug)
		user = get_object_or_404(society.members, pk=request.user.id)
		return render(request, 'main/member_requests.html', {'society': society})

def accept_join_request(request,slug,user_index):
		society = get_object_or_404(Society, slug=slug)
		if society.members.get(pk=request.user.id):
			user = society.member_requests.get(pk=user_index)
			society.member_requests.remove(user)
			society.members.add(user)
			return redirect('/'+slug+'/member_requests')
		else:
			return request('no_permission')

def reject_join_request(request,slug,user_index):
		society = get_object_or_404(Society, slug=slug)
		if society.members.get(pk=request.user.id):
			user = society.member_requests.get(pk=user_index)
			society.member_requests.remove(user)
			return redirect('/'+slug+'/member_requests')
		else:
			return redirect('no_permission')


def create_society(request):
		form = SocietyForm
		if request.method == 'POST':
			form = SocietyForm(request.POST)
			if form.is_valid():
				new_society = form.save()
				new_society.members.add(request.user)
			return redirect('/')

def society_page(request, slug):
		society = get_object_or_404(Society, slug=slug)
		return render(request, 'societies/home.html', {'society' : society})

def society_book_keeping(request, slug):
		society = get_object_or_404(Society, slug=slug)
		account = society.account
		if request.method == 'POST':
				form = TransactionForm(request.POST, request.FILES)
				if form.is_valid():
					form.save()
					return redirect('/'+slug+'/transactions')
		transaction_form = TransactionForm(initial={'account': account})
		return render(request, 'societies/book-keeping.html', {'account' : account, 'form' : transaction_form})