from django.shortcuts import render, redirect
from .forms import IncidentForm
from .models import Incident
from django.views.decorators.http import require_POST

# Create your views here.
# add a new view function called incident_create
def  home (request): 
    #incident = Incident.objects.get(pk=1)
    return render(request,'index.html')

def incident_create(request):
    if request.method == 'POST':
        
        #form = IncidentForm(request.POST)
        userform = IncidentForm(request.POST)

        #if form.is_valid():
        if userform.is_valid():

            #form.save()
            userform.save()
            
            print('form submitted')
            return redirect('incident_create')
    else:
        print('unable to submit')
        
        #form = IncidentForm()
        userform = IncidentForm()
    
    return render(request,
    'incident_create.html',
    {
        #'form': form
        'form': userform
    })
