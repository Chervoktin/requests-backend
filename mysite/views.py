from django.shortcuts import render
from django import forms
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from mysite.models import Person
import json
from django.core import serializers


class SumForm(forms.Form):
    a = forms.DecimalField()
    b = forms.DecimalField()


@csrf_exempt
def sum(request):
    if request.method == 'POST':
        form = SumForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['a'] + form.cleaned_data['b'])
        else:
            return HttpResponse(json.dumps(form.errors))

def persons(request):
    if request.method == 'GET':
        qset = Person.objects.all().values()
        return JsonResponse(list(qset),safe=False) 
