from .models import Incident
from django import forms
import django_filters

'''
class ResponsesFilter(django_filters.FilterSet):
    class Meta:
        model = Incident
        fields = ['accident_location', 'local_government_area', 'date_of_accident', 'time_of_accident', 'number_of_vehicles_involved', 'vehicle_type', 'vehicles_number_plates', 'vehicles_precrash_factors', 'road_geometry', 'road_type', 'driver_precrash_factors', 'collision_type', 'number_of_victims', 'number_of_injured', 'number_of_deaths', 'category_of_victims', 'victims_age_group', 'number_of_male_victims', 'number_of_female_victims', 'number_of_child_victims', 'victims_current_location']
'''

class ResponsesFilter(django_filters.FilterSet):
    month_of_accident = django_filters.NumberFilter(field_name='date_of_accident', lookup_expr='month')
    month_of_accident_gte = django_filters.NumberFilter(field_name='date_of_accident', lookup_expr='month__gte')
    month_of_accident_lte = django_filters.NumberFilter(field_name='date_of_accident', lookup_expr='month__lte')
    year_of_accident = django_filters.NumberFilter(field_name='date_of_accident', lookup_expr='year')
    year_of_accident_gte = django_filters.NumberFilter(field_name='date_of_accident', lookup_expr='year__gte')
    year_of_accident_lte = django_filters.NumberFilter(field_name='date_of_accident', lookup_expr='year__lte')
    #vehicles_precrash_factors = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Incident
        #fields = ['accident_location', 'vehicles_precrash_factors', 'road_geometry', 'road_type', 'driver_precrash_factors', 'collision_type', 'victims_current_location']
        fields = ['accident_location']
