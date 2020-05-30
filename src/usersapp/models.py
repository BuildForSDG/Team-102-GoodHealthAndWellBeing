from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

VEHICLE_CHOICES = (('Car saloon', 'Car saloon'),
            ('Microbus', 'Microbus (< 10 seater)'),
            ('Minibus', 'Minibus (< 15 seater)'),
            ('Coaster', 'Coaster (< 15 > 35 seater)'),
            ('Bus', 'Bus (> 35 seater)'),
            ('Pickup', 'Pickup'),
            ('SUV', 'SUV (Jeep'),
            ('Light lorry', 'Light lorry (< 3.5 t)'),
            ('Heavy lorry', 'Heavy lorry (> 3.5 t)'),
            ('Tanker', 'Tanker'),
            ('Trailer', 'Trailer'),
            ('Motorcycle', 'Motorcycle'),
            ('Tricycle', 'Tricycle'),
            ('Bicycle', 'Bicycle'),
            ('Unknown', 'Unknown'))

VEHICLE_PRECRASH_CHOICES = (('Tyre burst', 'Tyre burst'),
            ('Mechanical deficiency', 'Mechanical deficiency'),
            ('Overloaded', 'Overloaded'),
            ('Defective light', 'Defective light'),
            ('Nothing notable', 'Nothing notable'))

DRIVER_PRECRASH_CHOICES = (('Nothing notable', 'Nothing notable'),
            ('Fatigue/Sleepiness', 'Fatigue/Sleepiness'),
            ('Sudden illness', 'Sudden illness'),
            ('Speeding', 'Speeding'),
            ('Careless overtaking', 'Careless overtaking'),
            ('Tailgating', 'Tailgating'),
            ('Sudden turn', 'Sudden turn'),
            ('risktaking', 'Other calculated risktaking'),
            ('phone while driving', 'Use of phone while driving'),
            ('Alcohol', 'Influence of alcohol'),
            ('Drug', 'Influence of drug'),
            ('Other distractions', 'Other distractions/inattentiveness'))

VICTIM_GENDER = (('Male', 'Male'),
            ('Female', 'Female'))

VICTIM_CATEGORY = (('Driver', 'Driver'),
            ('Passenger', 'Passenger'),
            ('Trailer', 'Trailer'),
            ('Motorcycle', 'Motorcyclist'),
            ('Tricyclist', 'Tricyclist'),
            ('Bicyclist', 'Bicyclist'),
            ('Pedestrian', 'Pedestrian'))

VICTIM_AGE_GROUP= (('Baby', 'Baby'),
            ('Toddler', 'Toddler'),
            ('Child', 'Child'),
            ('Teenager', 'Teenager'),
            ('Adult', 'Adult'),
            ('Middle aged', 'Middle aged'),
            ('Elderly', 'Elderly'))
LOCATIONS = ((1, 'Accident Scene'),
            (2, 'Hospital'),
            (3, 'Other'))

LOCATIONS = ((1, 'Accident Scene'),
(2, 'Hospital'),
(3, 'Other'))


VICTIMS_LOCATIONS = ((1, 'Accident Scene'),
            (2, 'Hospital'),
            (3, 'Other'))

USER_LOCATION = [
    ('Abia', 'Abia'),
    ('Adamawa', 'Adamawa'),
    ('Akwa Ibom', 'Akwa Ibom'),
    ('Anambra', 'Anambra'),
    ('Bauchi', 'Bauchi'),
    ('Benue','Benue'),
    ('Borno', 'Borno'),
    ('Cross River', 'Cross River'),
    ('Damaturu', 'Damaturu'),
    ('Ebonyi', 'Ebonyi'),
    ('Enugu', 'Enugu'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun')
]

GEOMETRY_CHOICES = [
    ('Straight road', 'Straight road'),
    ('Curve', 'Curve'),
    ('Roundabout', 'Roundabout'),
    ('T-junction', 'T-junction'),
    ('Y-junction', 'Y-junction'),
    ('+-junction', '+-junction'),
    ('Bridge', 'Bridge'),
    ('Road works', 'Road works'),
    ('Other', 'Other')
]

ROAD_TYPE_CHOICES = [
    ('Dual carriageway', 'Dual carriageway'),
    ('Single carriageway', 'Single carriageway'),
    ('Expressway', 'Expressway'),
    ('Street', 'Street'),
    ('Other', 'Other')
]

COLLISION_CHOICES = [
    ('Mv/mv head on', 'Moving vehicles, head on'),
    ('Mv/mv rear end', 'Moving vehicles, rear end'),
    ('Mv/mv intersecting', 'Moving vehicles, intersecting'),
    ('Mv/mv overtake', 'Moving vehicles, overtake'),
    ('Mv/mv turn', 'Moving vehicles, turn'),
    ('Single mv hit object', 'Single moving vehicle, hit object'),
    ('Single mv run off', 'Single moving vehicle, run off'),
    ('Single mv falling off', 'Single moving vehicle, falling off'),
    ('Mv/pedestrian', 'Moving vehicle with pedestrian'),
    ('Mv/bicyclist', 'Moving vehicle with pedestrian'),
    ('Other', 'Other')
]

class Incident(models.Model) :
    location=models.CharField(choices=USER_LOCATION,max_length=45,null=False,blank=False)
    date_of_accident=models.DateField(auto_now=False)
    time_of_accident=models.TimeField(auto_now=False)
    number_of_vehicles_involved=models.IntegerField(null=False,blank=False)
    vehicle_type=MultiSelectField(choices=VEHICLE_CHOICES,max_length=50,null=False,blank=False)
    vehicles_number_plates=models.CharField(max_length=45,null=True,blank=True)
    vehicle_precrash_factors=MultiSelectField(choices=VEHICLE_PRECRASH_CHOICES,max_length=50,null=True,blank=True)
    number_of_damaged_vehicles=models.IntegerField(null=True,blank=True)
    road_geometry=models.CharField(choices=GEOMETRY_CHOICES,max_length=30,null=False,blank=False)
    road_type=models.CharField(choices=ROAD_TYPE_CHOICES,max_length=30,null=False,blank=False)
    driver_precrash_factors=MultiSelectField(choices=DRIVER_PRECRASH_CHOICES,max_length=50,null=False,blank=False)
    collision_type=models.CharField(choices=COLLISION_CHOICES,max_length=70,null=False,blank=False)
    number_of_victims=models.IntegerField(null=True,blank=True)
    number_of_injured=models.IntegerField(null=True,blank=True)
    number_of_deaths=models.IntegerField(null=True,blank=True)
    category_of_victims=MultiSelectField(choices=VICTIM_CATEGORY,max_length=30,null=False,blank=False)
    gender_of_victims=MultiSelectField(choices=VICTIM_GENDER,max_length=20,null=False,blank=False)
    victims_age_group=MultiSelectField(choices=VICTIM_AGE_GROUP,max_length=20,null=False,blank=False)
    number_of_male_victims=models.IntegerField(null=True,blank=True)
    number_of_female_victims=models.IntegerField(null=True,blank=True)
    number_of_child_victims=models.IntegerField(null=True,blank=True)
    victims_current_location=MultiSelectField(choices=VICTIMS_LOCATIONS,max_length=50,null=False,blank=False)
    if_hospital_specify=models.CharField(max_length=45,null=True,blank=True)
    if_other_location_specify=models.CharField(max_length=45,null=True,blank=True)
    more_accident_info=models.TextField(blank=True,null=True)