from django.shortcuts import render

# Create your views here.
from django.apps import apps
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
import short_url


def redirect_view(request, tiny):
    """
    Redirect to a given object from a short URL.
    """

    model = apps.get_model('MYAPP', 'MYBLOG')
    try:
        id = short_url.decode_url(tiny)
    except ValueError:
        raise Http404('Bad encoded ID.')

    # Try to look up the object. If it's not a valid object, or if it doesn't
    # have an absolute url, bail again.
    obj = get_object_or_404(model, pk=id)
    return redirect(obj)
