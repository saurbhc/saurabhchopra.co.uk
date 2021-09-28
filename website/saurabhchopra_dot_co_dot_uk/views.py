from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request: object):
    context = {}
    return render(request, "saurabhchopra_dot_co_dot_uk/index.html", context)

def favicon(request: object):
    context = {}
    image_data = open("/home/saurabhchopra0108/saurabhchopra.co.uk/website/saurabhchopra_dot_co_dot_uk/static/saurabhchopra_dot_ac_dot_uk/favicon.ico", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
