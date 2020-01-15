from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
import json

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
 
