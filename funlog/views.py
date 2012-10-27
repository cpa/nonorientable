from django.shortcuts import render_to_response
from funlog.models import Funfact
from django.http import HttpResponse

def index(request):
    funfact = Funfact.objects.all().order_by('-pub_date')[0]
    return render_to_response('funlog/index.html', {'funfact': funfact})

