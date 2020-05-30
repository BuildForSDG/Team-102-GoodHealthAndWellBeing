from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.forms import ModelForm
from .models import Incident

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'date_of_accident', 'time_of_accident', 'number_of_vehicles_involved', 'vehicle_type', 'vehicles_number_plates', 'vehicle_precrash_factors', 'number_of_damaged_vehicles', 'road_geometry', 'road_type', 'driver_precrash_factors', 'collision_type', 'number_of_victims', 'number_of_injured', 'number_of_deaths', 'category_of_victims', 'gender_of_victims', 'victims_age_group', 'number_of_male_victims', 'number_of_female_victims', 'number_of_child_victims', 'victims_current_location', 'if_hospital_specify', 'if_other_location_specify', 'more_accident_info']
        widgets = {
                    'date_of_accident': DatePickerInput(), # default date-format %m/%d/%Y will be used
                    # 'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
                    'time_of_accident': TimePickerInput(),
                }