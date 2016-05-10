from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

from django.http import HttpResponse
import datetime

def helloworld(request):
    return HttpResponse("hello ado i sss")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))

    return HttpResponse(html)

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'

    return HttpResponse(request)

def search_form(request):

    return render_to_response('search_form.html')
