from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {}
    return render(request, 'qa/index.html', context)
