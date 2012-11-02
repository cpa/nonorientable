from django.shortcuts import render_to_response
from funlog.models import Funfact
from django.http import HttpResponse

def index(request):
    funfact = Funfact.objects.all().order_by('-pub_date')[0]
    return render_to_response('funlog/index.html', {'funfact': funfact})

def funfactsall(request):
    funfacts = Funfact.objects.all().order_by('-pub_date')
    return render_to_response('funlog/all.html', {'funfacts': funfacts})

def apropos(request):
    return render_to_response('funlog/apropos.html')

def legal(request):
    return render_to_response('funlog/legal.html')

def detail(request, url):
    funfact = Funfact.objects.get(urltext=url)
    return render_to_response('funlog/index.html', {'funfact': funfact})
