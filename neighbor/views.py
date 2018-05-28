# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Neighborhood Watch'
    return render(request, 'home/home.html', {"title": title})
