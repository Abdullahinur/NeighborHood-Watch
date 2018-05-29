# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})

            
@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Neighborhood Watch'
    return render(request, 'home/home.html', {"title": title})


@login_required
def profile_view(request):
    user = request.user
    form = EditProfileForm(initial={'first_name':user.first_name, 'last_name': user.last_name})
    context = {
        "form": form
    }
    return render(request, 'registration/profile.html', context)
