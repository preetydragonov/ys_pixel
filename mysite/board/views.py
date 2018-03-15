# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def searched_board(request):
    return render(request, 'board/index.html', {})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
