# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.template import  loader
from django.shortcuts import render
from django.http import HttpResponse
from .functions import *
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
    myfile = request.FILES['upload']
    fs = FileSystemStorage(location='tosplit/')
    n=myfile.name
    #print n
    n=n.replace(" ","_")
    filename = fs.save(n, myfile)
    #print filename
    uploaded_file_url = fs.url(filename)
    path=fs.location+(' \ ').strip()+uploaded_file_url
    #print path
    temp=loader.get_template('utils/download.html')
    context={}

    if(function_split(rng,path)):
        return HttpResponse(temp.render(context, request))
    else:
        return HttpResponse('something went wrong')

def download(request):
    response = HttpResponse(open('todownload/download.zip', 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=download.zip'
    return response