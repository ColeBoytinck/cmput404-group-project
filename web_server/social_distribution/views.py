from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    if request.method == 'GET':
        return redirect(reverse('user_stream'))
    else:
        return HttpResponse('404 Error', status=404)