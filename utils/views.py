# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import  loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    temp=loader.get_template('utils/home.html')
    context={}
    return HttpResponse(temp.render(context,request))

def merge(request):
    temp=loader.get_template('utils/merge.html')
    context={}
    return HttpResponse(temp.render(context,request))

def split(request):
    temp=loader.get_template('utils/split.html')
    context={}
    return HttpResponse(temp.render(context,request))

def rotate(request):
    temp=loader.get_template('utils/rotate.html')
    context={}
    return HttpResponse(temp.render(context,request))