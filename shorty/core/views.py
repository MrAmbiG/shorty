from django.shortcuts import render
from django.template import RequestContext
from django.urls import resolve
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.utils import timezone
import pytz
# Create your views here.


def handler404(request):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler404(request):
    response = render('500.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 500
    return response


def shorty(request):
    return render(request, 'shorty.html')
