from django.db import models

# Create your models here.
class Incident(models.Model) :
    location=models.CharField(max_length=45,null=False,blank=False)
    date=models.DateField()
    description=models.TextField(blank=True,null=True)
    vehicle_type=models.CharField(max_length=20,null=False,blank=False)
    vehicle_involved=models.CharField(max_length=20,null=False,blank=False)
    traffic_lane=models.CharField(max_length=20,null=True,blank=True)
    road_type=models.CharField(max_length=20,null=True,blank=True)
    junction_type=models.CharField(max_length=20,null=True,blank=True)
    time=models.TimeField( )
    causes=models.CharField(max_length=30,null=True,blank=True)
    collision_type=models.CharField(max_length=100,null=True,blank=True)
    number_of_victims=models.CharField(max_length=20,null=True,blank=True)
    number_of_injury=models.CharField(max_length=10,null=True,blank=True)
    number_of_death=models.CharField(max_length=10,null=True,blank=True)
    number_of_damage_vehicle=models.CharField(max_length=10,null=True,blank=True)
    currently_allocated_to=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    age=models.CharField(max_length=20,null=True,blank=True)