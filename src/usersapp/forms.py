from django.forms import ModelForm
from .models import Incident

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'date_of_accident', 'time_of_accident', 'number_of_vehicles_involved', 'vehicle_type', 'vehicle_precrash_factors', 'number_of_damaged_vehicles', 'road_geometry', 'road_type', 'driver_precrash_factors', 'collision_type', 'number_of_victims', 'number_of_injured', 'number_of_deaths', 'category_of_victims', 'gender_of_victims', 'victims_age_group', 'victims_current_location', 'more_accident_info']


