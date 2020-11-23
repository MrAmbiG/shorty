from django.shortcuts import render
from django.template import RequestContext
from django.urls import resolve
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.utils import timezone
import pytz
import random
import string
LENGTH = 5
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
    template = 'shorty.html'
    if request.method == 'POST':
        form = shorties_form(request.POST or None)
        if form.is_valid():
            original = str(form.cleaned_data['original']).lower()
            alias = form.cleaned_data['alias']
            ranstring = ''.join(random.choice(letters) for i in range(LENGTH))
            while not shorties.objects.filter(alias=ranstring).exists():
                ranstring = ''.join(random.choice(letters)
                                    for i in range(LENGTH))
            s, created = shorties.objects.get_or_create(
                original=original, alias=ranstring)
            s.save()
            response = {"alias": alias, "original": original}
            return render(request, "result.html", response)
    else:
        return render(request, template, {'form': form})
