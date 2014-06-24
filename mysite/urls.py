#! /usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url
#from mysite.views.view import search_form,display_meta,current_datetime,hours_ahead
from django.conf.urls import *
from django.contrib import admin
#from mysite.books import views
#from mysite.contact.views import contact
admin.autodiscover()


#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'mysite.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#	url(r'^hello/$','mysite.books.views.display_meta'),
#	url(r'^time/$','mysite.books.views.current_datetime'),
#	url(r'^time/plus/(\d{1,2})/$','mysite.books.views.hours_ahead'),
#	url(r'^search_form/$','mysite.books.views.search_form'),
#	url(r'^search/$','mysite.books.views.search'),
#	url(r'^contact/$','mysite.contact.views.contact'),
#    url(r'^admin/', include(admin.site.urls)),
#)
urlpatterns = patterns('mysite.books.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^hello/$','display_meta'),
	url(r'^time/$','current_datetime'),
	url(r'^time/plus/(\d{1,2})/$','hours_ahead'),
	url(r'^search_form/$','search_form'),
	url(r'^search/$','views.search'),
    url(r'^admin/', include(admin.site.urls)),
)
