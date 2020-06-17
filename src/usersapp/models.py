from django.db import models
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
import pytz
from datetime import date

# Create your models here.



class Incident(models.Model) :

    VEHICLE_CHOICES = (('Car saloon', 'Car saloon'),
                ('Microbus', 'Microbus (< 10 seater)'),
                ('Minibus', 'Minibus (< 15 seater)'),
                ('Coaster', 'Coaster (< 15 > 35 seater)'),
                ('Bus', 'Bus (> 35 seater)'),
                ('Pickup', 'Pickup'),
                ('SUV', 'SUV (Jeep)'),
                ('Light lorry', 'Light lorry (< 3.5 t)'),
                ('Heavy lorry', 'Heavy lorry (> 3.5 t)'),
                ('Tanker', 'Tanker'),
                ('Trailer', 'Trailer'),
                ('Motorcycle', 'Motorcycle'),
                ('Tricycle', 'Tricycle'),
                ('Bicycle', 'Bicycle'),
                ('Unknown', 'Unknown'),
                ('Other', 'Other'))

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

    VICTIM_CATEGORY = (('Driver', 'Driver'),
                ('Passenger', 'Passenger'),
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
        ('FCT', 'FCT'),
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue','Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Enugu', 'Enugu'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara')
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

    USER_CATEGORY = [
                ('Victim', 'Accident victim'),
                ('Eye nitness', 'Eye witness'),
                ('Driver', 'Driver of a vehicle in the accident'),
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
        ('Mv/motorcyclist', 'Moving vehicle with motorcyclist'),
        ('Mv/bicyclist', 'Moving vehicle with bicyclist'),
        ('Other', 'Other')
    ]
    
    your_category=models.CharField(choices=USER_CATEGORY,max_length=30,null=False,blank=False, db_column='User category')
    if_other_category_specify=models.CharField(max_length=50,null=True,blank=True, db_column='User other category')
    accident_location=models.CharField(choices=USER_LOCATION,max_length=45,null=False,blank=False)
    local_government_area=models.CharField(max_length=25,null=False,blank=False, db_column='LGA')
    address_or_nearest_landmark=models.CharField(max_length=50,null=False,blank=False, help_text="By landmark we mean somewhere notable such as bustop, market, hotel, hospital etc.", verbose_name="address and/or nearest landmark")
    date_of_accident=models.DateField(auto_now=False)
    time_of_accident=models.TimeField(auto_now=False)
    number_of_vehicles_involved=models.PositiveIntegerField(null=False,blank=False, db_column='vehicles involved', help_text="Number of vehicles can be zero or more.")
    vehicle_type=MultiSelectField(choices=VEHICLE_CHOICES,max_length=50,null=False,blank=False)
    if_other_vehicle_specify=models.CharField(max_length=50,null=True,blank=True, db_column='other vehicle type')
    vehicles_number_plates=models.CharField(max_length=100,null=True,blank=True, help_text="You can add more than one vehicle number plate seperated by a comma.")
    vehicles_precrash_factors=MultiSelectField(choices=VEHICLE_PRECRASH_CHOICES,max_length=50,null=False,blank=False, help_text="This field is required")
    road_geometry=models.CharField(choices=GEOMETRY_CHOICES,max_length=30,null=False,blank=False)
    road_type=models.CharField(choices=ROAD_TYPE_CHOICES,max_length=30,null=False,blank=False)
    driver_precrash_factors=MultiSelectField(choices=DRIVER_PRECRASH_CHOICES,max_length=50,null=False,blank=False, help_text="This field is required")
    collision_type=models.CharField(choices=COLLISION_CHOICES,max_length=70,null=False,blank=False)
    number_of_victims=models.PositiveIntegerField(null=False,blank=False, help_text="Number of victims can be zero or more.")
    number_of_injured=models.PositiveIntegerField(null=False,blank=False, help_text="Number of injured can be zero or more.")
    number_of_deaths=models.PositiveIntegerField(null=False,blank=False, help_text="Number of dead can be zero or more.")
    category_of_victims=MultiSelectField(choices=VICTIM_CATEGORY,max_length=40,null=True,blank=True, help_text="If no victim, leave boxes unticked.")
    victims_age_group=MultiSelectField(choices=VICTIM_AGE_GROUP,max_length=50,null=True,blank=True,help_text="If no victim, leave boxes unticked.")
    number_of_male_victims=models.PositiveIntegerField(null=False,blank=False, help_text="Number of male victims can be zero or more.")
    number_of_female_victims=models.PositiveIntegerField(null=False,blank=False, help_text="Number of female victims can be zero or more")
    number_of_child_victims=models.PositiveIntegerField(null=False,blank=False, help_text="Number of child victims can be zero or more")
    victims_current_location=MultiSelectField(choices=VICTIMS_LOCATIONS,max_length=50,null=True,blank=True,help_text="If no victim, leave box unticked.")
    if_hospital_specify=models.CharField(max_length=50,null=True,blank=True, db_column='hospital location')
    if_other_location_specify=models.CharField(max_length=50,null=True,blank=True, db_column='other location')
    more_accident_info=models.TextField(blank=True,null=True)
    videofile= models.FileField(upload_to='videos/', null=True, blank=True, verbose_name="upload a video or an image")
    
    #calling objects used in responder and search_responses function from views.py
    objects = models.Manager()

    #writing validation function
    def clean(self) -> None:
        today = date.today()
        if self.date_of_accident > today:
                raise ValidationError(
                    'Date of accident cannot be in the future'
                )
        
        if self.number_of_injured > self.number_of_victims:
                raise ValidationError(
                    'Number of injured cannot be greater than number of victims'
                )
        if self.number_of_deaths > self.number_of_victims:
                raise ValidationError(
                    'Number of deaths cannot be greater than number of victims'
                )

        if (self.number_of_injured + self.number_of_deaths)  > self.number_of_victims:
                raise ValidationError(
                    'Number of injured and deaths cannot be greater than number of victims'
                )

        if self.vehicle_type == '':
                raise ValidationError(
                    'Vehicle type cannot be empty'
                )

        if self.vehicles_precrash_factors == '':
                raise ValidationError(
                    'Vehicles precrash factors cannot be empty'
                )
        if self.driver_precrash_factors == '':
                raise ValidationError(
                    'Driver precrash factors cannot be empty'
                )
        if self.number_of_male_victims > self.number_of_victims:
                raise ValidationError(
                    'Number of male victims cannot be greater than number of victims'
                )
        if self.number_of_female_victims > self.number_of_victims:
                raise ValidationError(
                    'Number of female victims cannot be greater than number of victims'
                )
        if self.number_of_child_victims > self.number_of_victims:
                raise ValidationError(
                    'Number of child victims cannot be greater than number of victims'
                )
        if (self.number_of_male_victims + self.number_of_female_victims)  > self.number_of_victims:
                raise ValidationError(
                    'Sum of male and female victims cannot be greater than number of victims'
        )
        if (self.number_of_male_victims + self.number_of_child_victims)  > self.number_of_victims:
                raise ValidationError(
                    'Sum of male and child victims cannot be greater than number of victims'
        )
        if (self.number_of_female_victims + self.number_of_child_victims)  > self.number_of_victims:
                raise ValidationError(
                    'Sum of female and child victims cannot be greater than number of victims'
        )
        if (self.number_of_male_victims + self.number_of_female_victims + self.number_of_child_victims)  > self.number_of_victims:
                raise ValidationError(
                    'Sum of male, female and child victims cannot be greater than number of victims'
        )