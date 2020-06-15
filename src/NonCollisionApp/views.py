from django.shortcuts import render
from django.db import models
from NonCollisionApp.models import ResponseDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import ResponseModelForm

# Create your views here.

def responseDetails(request):
    if request.method == 'POST':
        form = ResponseModelForm(request.POST)
        if form.is_valid():
            form.save()
            responses = ResponseDetails.objects.all()

            return render(request, 'responsepage.html', {'responses': responses})

    else:
        form_class = ResponseModelForm

    return render(request, 'page.html', {'form': form_class,})