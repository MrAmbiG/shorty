from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import shorties
from .forms import shorties_form
from django.utils.crypto import get_random_string
LENGTH = 5

# Create your views here.
letters = ['a', 'c', 'd', 'e', 'g', 'i', 'k', 'l',
           'm', 'n', 'q', 'r', 's', 't', 'u', 'x', 'y', 'z', '2', '3', '4', '5', '6', '7', '8', '9']


def create_new_ref_number():
    alias = get_random_string(length=LENGTH, allowed_chars=letters)
    check = shorties.objects.filter(alias=alias).exists()
    if check:
        create_new_ref_number()
    else:
        return alias


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
            alias = create_new_ref_number()
            original = str(form.cleaned_data['original']).lower()
            if 'https:' in original:
                https = True
            else:
                https = False
            if not shorties.objects.filter(original=original).exists():
                s, created = shorties.objects.get_or_create(
                    original=original, alias=alias, https=https)
                s.save()
            else:
                obj = shorties.objects.filter(original=original)[0]
                alias = obj.alias
                https = obj.https
            context = {}
            context['alias'] = alias
            context['original'] = original
            context['https'] = https
            return render(request, "result.html", context)
    else:
        print('form is not valid or not POST')
        return render(request, template, {'form': form})


def reroute(request, id):
    url = request.META['HTTP_HOST']
    if shorties.objects.filter(alias=str(id)).exists():
        url = shorties.objects.filter(alias=id)[0].original
    print(url)
    return redirect(url)
