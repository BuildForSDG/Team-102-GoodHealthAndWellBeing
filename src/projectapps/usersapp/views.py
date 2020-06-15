import pytz
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncidentForm
from .models import Incident
from django.views.decorators.http import require_POST
from .filters import ResponsesFilter

# Create your views here.
# add a new view function called incident_create
def  home (request): 
    #incident = Incident.objects.get(pk=1)
    return render(request,'index.html')

def incident_create(request):
    if request.method == 'POST':

       # lastvideo= Incident.objects.last()
        
        #videofile= lastvideo.videofile
        
        #form = IncidentForm(request.POST)
        userform = IncidentForm(request.POST, request.FILES)

        #if form.is_valid():
        if userform.is_valid():

            #form.save()
            userform.save()
            
            print('form submitted')
            messages.info(request, 'Thank you for reporting')
            return redirect('incident_create')
    else:
        print('Unable to submit')

        #form = IncidentForm()
        userform = IncidentForm()
    
    return render(request,
    'incident_create.html',
    {
        #'videofile': videofile,
        #'form': form
        'form': userform
    })


#this function generates users' report responses into a single table
def responder(request):
    #detail=Incident.objects.all().filter(accident_location__exact='Adamawa')
    detail=Incident.objects.all()
    return render(request,
    'responder.html',
    {
        'detail': detail
    })

'''
#getting responders timezone when searching users responses 

def convert_to_localtime(utctime):
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz
'''

#writing a function that would filter fields in ResponsesFilter in filters.py
def search_responses(request):
    responses = Incident.objects.all()
    response_filter = ResponsesFilter(request.GET, queryset=responses)
   # has_filter = any(field in request.GET for field in set(response_filter.get_fields()))
    return render(request, 
    'search_responses.html', 
    {'filter': response_filter
    })