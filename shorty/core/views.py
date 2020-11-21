from django.shortcuts import render
from django.template import RequestContext
from django.urls import resolve
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.utils import timezone
import pytz
# Create your views here.
letters = ['a', 'c', 'd', 'e', 'g', 'i', 'k', 'l',
           'm', 'n', 'q', 'r', 's', 't', 'u', 'x', 'y', 'z', '2', '3', '4', '5', '6', '7', '8', '9']


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
    form = shorties_form()
    template_name = 'shorty.html'
    # s, created = shorties.objects.get_or_create(alias=alias)
    return render(request, 'shorty.html')
