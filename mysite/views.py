from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

class SumForm(forms.Form):
    a = forms.DecimalField()
    b = forms.DecimalField()

@ensure_csrf_cookie
def sum(request):
    if request.method == 'POST':
        form = SumForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['a'] + form.cleaned_data['b'])
 
