# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.template import  loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    temp=loader.get_template('utils/home.html')
    context={}
    return HttpResponse(temp.render(context,request))

def merge(request):
    request.session['id']=3135153
    s=request.session['id']
    temp=loader.get_template('utils/merge.html')
    context={'s':s}
    return HttpResponse(temp.render(context,request))

def split(request):
    temp=loader.get_template('utils/split.html')
    context={}
    return HttpResponse(temp.render(context,request))

def rotate(request):
    temp=loader.get_template('utils/rotate.html')
    context={}
    return HttpResponse(temp.render(context,request))

def split_do(request):
    single=request.POST['single']
    rng=''
    if(single=='2'):
        rng=request.POST['range']
    print single,rng
    myfile = request.FILES['upload']
    fs = FileSystemStorage(location='media/')
    #print(fs.location)
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    #print(uploaded_file_url)
    return HttpResponse('uploaded file '+uploaded_file_url+" to "+fs.location)