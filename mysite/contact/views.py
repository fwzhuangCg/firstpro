#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse 
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from mysite.books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from mysite.contact.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm()
	return render_to_response('contact_form.html', {'form': form})
	
		
