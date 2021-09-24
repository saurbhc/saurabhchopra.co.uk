from django.shortcuts import render


# Create your views here.

def index(request: object):
    context = {}
    return render(request, "saurabhchopra_dot_co_dot_uk/index.html", context)
