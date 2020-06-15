from django.forms import ModelForm
from NonCollisionApp .models import ResponseDetails
from django.forms import Textarea

class ResponseModelForm(ModelForm):
    class Meta:
        model = ResponseDetails
        fields = ['Incident_happening', 'State', 'LG_Area' , 'Along_the_Way',

                  'Description_Of_the_Area', 'Photo_of_Area']
        widgets = {
            'Description_Of_the_Area': Textarea(attrs={'cols': 60, 'rows': 10}),
            'Along_the_Way': Textarea(attrs={'cols': 60, 'rows': 2})

        }
