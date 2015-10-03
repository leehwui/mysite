import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, world!")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'dateapp/current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours, it will be %s" % (offset, dt)
    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td>' % (k, v))

    return HttpResponse('<table>%s</table>' % '\n'.join(html))
