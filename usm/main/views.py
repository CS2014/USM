'''
		author: Ross Kinsella
		date:   2014/feb/13

		The first nesting of the URL paths.
		Currently the user selects | creates a society at this point.
'''

from django.shortcuts import render, render_to_response, redirect
from main.models import Society
from main.models import SocietyForm

def index(request):
		print 'INDEX RECEIVED REQUEST: ' + request.method
		society_list = Society.objects.all()
		form = SocietyForm
		context = {'society_list': society_list, 'form': form}
		return render(request, 'main/index.html', context)

def create_society(request):
		print 'CREATE_SOCIETY RECEIVED REQUEST: ' + request.method
		form = SocietyForm
		if request.method == 'POST':
			form = SocietyForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
			return redirect('/main')