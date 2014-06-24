#! /usr/bin/env python
#coding=utf-8
from django.shortcuts import render
from django.http import Http404,HttpResponse 
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from mysite.books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

import datetime
def display_meta(request):
	values = request.META.items()
	values.sort()
	#return HttpResponse("Hello world")
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
	#return render_to_response('display_meta.html',{'html':html})

def current_datetime (request):
	now = datetime.datetime.now()
	#example1
	#html = "<html><body>It is now %s.</body></html>" %now
	#return HttpResponse(html)
	
	#example2
	#t = Template("<html><body>It is now {{ current_date}}.</body></html>")
	#html = t.render(Context({"current_date":now}))
	#return HttpResponse(html)
	
	#example3
	#t = get_template('current_datetime.html')
	#html = t.render(Context({"current_date":now}))
	#return HttpResponse(html)

	#example4
	return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	#example1
	#dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#html ="<html><body>In %s hour(s),it will be %s.</body></html>" %(offset,dt)
	#return HttpResponse(html)

	#example2
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('future_datetime.html',{'hour_offset':offset,'next_time':dt})

def search_form(request):
	return render_to_response('search_form.html')
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html',
				{'books':books,'query':q})
	return render_to_response('search_form.html', {'errors': errors})
	
	#if 'q' in request.GET and request.GET['q']:
		#q = request.GET['q']
		#books = Book.objects.filter(title__icontains=q)
		#return render_to_response('search_results.html',
			#{'books':books,'query':q})
	#else:
		#return HttpResponse('Please submit a search term.')
		#return render_to_response('search_form.html', {'error': True})
	
def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	return render_to_response('contact_form.html',
		{'errors': errors,
		'subject': request.POST.get('subject', ''),
		'message': request.POST.get('message', ''),
		'email': request.POST.get('email', ''),
	})
	
	
	
		
