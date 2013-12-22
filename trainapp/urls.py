# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 20:31:47 2013

@author: amyskerry
"""

from django.conf.urls import patterns, url

from trainapp import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^home$', views.homepage, name='homepage'),
    url(r'^(?P<username>\w+)/chooseworkout$', views.chooseworkout, name='chooseworkout'),
    url(r'^(?P<username>\w+)/dataentry$', views.dataentry, name='dataentry'),
    # ex: /polls/5/results/
    url(r'^(?P<username>\w+)/metrics/$', views.metrics, name='metrics'),
    # ex: /polls/5/vote/
    url(r'^viewdata/$', views.viewdata, name='viewdata'),
    url(r'^(?P<username>\w+)/updated$', views.updated, name='updated'),
)