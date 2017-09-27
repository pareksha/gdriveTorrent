# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from mainApp.forms import *
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def downloadView(request):
    dictV = {}
    if request.method == 'POST':
        torrentUrl = request.POST.get('torrentUrl')
        print "URL",torrentUrl
    return render(request, 'download.html', dictV)

def loginView(request):
    dictV = {}
    form = loginForm()
    dictV['form'] = form
    if request.user.is_authenticated() and request.user.is_superuser:
        return HttpResponseRedirect('/download/')
    if request.user.is_authenticated() and request.user.is_staff:
        return HttpResponseRedirect('/download/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userObj = auth.authenticate(username=username,password=password)
        if userObj is not None:
            auth.login(request,userObj)
            if userObj.is_staff:
                return HttpResponseRedirect('/download/')
        else:
            dictV['error'] = 'Invalid username/password combination'
    return render(request, 'login.html', dictV)
