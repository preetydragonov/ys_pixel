#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def enterance(request):
    return render(request, 'enterance/searching_tab_2.html', {})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
