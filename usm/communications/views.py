from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from societymembers.models import *
from communications.tasks import *

def send_sms(request, slug):
    context = RequestContext(request)
    if request.method == 'POST':
        members = SocietyMember.objects.filter(id__in=request.POST.getlist("member_select"))
        send_sms_task(members=members, message_text=request.POST['txt_message'])
        #send_sms_task.apply(members=members, message_text=request.POST['txt_message'])
        return HttpResponseRedirect(reverse('main:dashboard', args=[slug]))
    else:
        members = SocietyMember.objects.filter(society__slug=slug)
        return render(request, 'communications/send_sms.html', {'context': context, 'slug': slug, 'members': members})

def send_email(request, slug):
    context = RequestContext(request)
    if request.method == 'POST':
        members = SocietyMember.objects.filter(id__in=request.POST.getlist("member_select"))
        send_email_task(members=members, message_text=request.POST['txt_message'], message_subject=request.POST['txt_subject'])
        #send_sms_task.apply(members=members, message_text=request.POST['txt_message'])
        return HttpResponseRedirect(reverse('main:dashboard', args=[slug]))
    else:
        members = SocietyMember.objects.filter(society__slug=slug)
        return render(request, 'communications/send_email.html', {'context': context, 'slug': slug, 'members': members})