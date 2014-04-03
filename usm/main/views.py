'''
        author: Ross Kinsella
        date:   2014/feb/13
'''
import json
from main.forms import UserCreateForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse

from main.models import Society
from main.models import SocietyForm
from accounting.models import Account, TransactionForm, Transaction

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''
Homepage views
'''
def homepage(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return user_homepage(request)
    else:
      return render(request, 'main/index.html', {'context': context})

# When the user has not selected the society they want to use.
def user_homepage(request):
    context = RequestContext(request)
    form = SocietyForm
    return render(request, 'main/user_homepage.html', {'context': context, 'form':form})

def request_membership(request):
        if request.method == 'POST':
            slug = request.POST['slug']
            try:
                society = get_object_or_404(Society, slug=slug)
                try:
                    society.members.get(pk=request.user.id)
                    data = json.dumps({"message" : "Your already a member of this society."})  
                except:              
                    society.member_requests.add(request.user)
                    data = json.dumps({"message" : "Your request has been sent. You will be notified when it is accepted."})                
            except (Http404):
                data = json.dumps({"message" : "No society with that code exists."})                
        print data
        return HttpResponse(data, content_type='application/json')
        

def create_society(request):
        form = SocietyForm
        if request.method == 'POST':
            form = SocietyForm(request.POST)
            if form.is_valid():
                new_society = form.save()
                new_society.members.add(request.user)
                account = Account(society = new_society)
                new_society.account = account
                account.save()
            return redirect('/') 

'''
Authentication views
'''
def user_login(request):

    if request.user.is_authenticated():
        return redirect("/")
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/banned_user")
        else:
            messages.add_message(request, messages.INFO, "Your user name and password do not match")
            return redirect("/login/")
    else:
        return render(request, 'main/login.html', {})

def signup(request):
        if request.method == 'POST':
            user_form = UserCreateForm(request.POST)
            if user_form.is_valid():
                    username = user_form.clean_username()
                    password = user_form.clean_password2()
                    user_form.save()
                    user = authenticate(username=username, password=password)                   
                    login(request, user)
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

'''
Logged in user views
'''     
def dash_board(request, slug): 
        try:
                society = get_object_or_404(Society, slug=slug)
                society.members.get(pk=request.user.id)
                monthlyTotals = society.account.tabulate_transactions_past_year_by_month()
                print(monthlyTotals)
                return render(request, 'accounting/index.html', {'society': society , 'monthlyTotals':monthlyTotals})
        except (Http404, User.DoesNotExist):
                messages.add_message(request, messages.INFO, 
                "You do not have permission to access that account.",
                extra_tags="permission")
                return redirect('/')

'''
Add users to account
'''
def member_requests(request,slug):
        try:
                society = get_object_or_404(Society, slug=slug)
                society.members.get(pk=request.user.id)
                return render(request, 'main/member_requests.html', {'society': society})
        except (Http404, User.DoesNotExist):
                messages.add_message(request, messages.INFO, 
                "You do not have permission to access that account.",
                extra_tags="permission")
                return redirect('/')

def accept_join_request(request,slug,user_index):
        try:
                society = get_object_or_404(Society, slug=slug)
                if society.members.get(pk=request.user.id):
                    user = society.member_requests.get(pk=user_index)
                    society.member_requests.remove(user)
                    society.members.add(user)
                    return redirect('/'+slug+'/member_requests')
        except (Http404, User.DoesNotExist):
                messages.add_message(request, messages.INFO, 
                "You do not have permission to access that account.",
                extra_tags="permission")
                return redirect('/')

def reject_join_request(request,slug,user_index):
        try:
                society = get_object_or_404(Society, slug=slug)
                if society.members.get(pk=request.user.id):
                    user = society.member_requests.get(pk=user_index)
                    society.member_requests.remove(user)
                    return redirect('/'+slug+'/member_requests')
        except (Http404, User.DoesNotExist):
                messages.add_message(request, messages.INFO, 
                "You do not have permission to access that account.",
                extra_tags="permission")
                return redirect('/')