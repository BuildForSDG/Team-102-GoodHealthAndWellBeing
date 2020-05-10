from django.db import models




# Create your models here.
class Vehicle(models.Model):
	VEHICLE_TYPE=[
	('Car','Car'),('Minibus','Minibus'),('Coaster','Coaster'),('Bus','Bus'),('Pickul','Pickup'),('Jeep','Jeep'),('Lorry','Lorry'),('Tanker','Tanker'),('Trailer','Trailer'),('Motorcycle','Motorcycle'),('Tricycle','Tricycle'),('Bicycle','Bicycle'),('Pedestrian','Pedestrian'),('Other','Other')	
	]
	
	Vehicle_type=models.CharField(max_length=20,choices=VEHICLE_TYPE,default='Car')

class Road_Environment(models.Model):
	TRAFFIC_LANE=[
	('One-Lane Road','one-lane road'),('Two-Lane Road','Two-Lane Road'),('Three-Lane','Three-Lane Road'),('Four-Lane Road','Four-Lane Road')	
	]
	WEATHER=[
	('Sunny','Sunny'),('Cloudy','Cloudy'),('Rainy','Rainy'),('Foggy','Foggy')	
	]
	ROAD_TYPE=[
	('Dual CarriageWay','Dual Carriage'),('Single CarriageWay','Single CarriageWay'),('ExpressWay','ExpressWay'),('Street','Street'),('Other','Other')	
	]
	JUNCTION_TYPE=[
	('RoundAbout','RoundAbout'),('Bridge','Bridge'),('T-Junction','T-Junction'),('Y-Junction','Y-Junction'),('Other','Other')	
	]
	traffic_lane=models.CharField(max_length=20,choices=TRAFFIC_LANE,default='One-Lane Road')
	road_type=models.CharField(max_length=20,choices=ROAD_TYPE,default='Street')
	junction_type=models.CharField(max_length=20,choices=JUNCTION_TYPE,default='T-Junction')
	weather=models.CharField(max_length=20,choices=WEATHER,default='Sunny')
class Crash_Information(models.Model):
	CAUSES=[
	('Unsual Driving','Unsual Driving'),('Reckless Driving','Reckless Driving'),('Sudden Lane Change','Sudden Lane Change'),('Drunk Driving','Drunk Driving'),('Equipment Failure','Equipment Failure'),('Driver Sleepiness','Driver Sleepiness')
	]
	COLLISION_TYPE=[
	('Head-on Collision','Head-on Collision'),('Collision Involving Pedestrian','Collision Involving Pedestrian'),('Single-Vehicle Collision','Single-Vehicle Collision'),('Intersection Collision','Intersection Collision'),('Other','Other')
	]
	location=models.CharField(max_length=100,unique=True)
	division=models.CharField(max_length=100,unique=True)
	year=models.CharField(max_length=50,unique=True,blank=True)
	month=models.CharField(max_length=50,unique=True,blank=True)
	date=models.DateField()
	time=models.TimeField( )
	causes=models.CharField(max_length=100,choices=CAUSES)
	collision_type=models.CharField(max_length=100,choices=COLLISION_TYPE,blank=False)
	
class Severitie(models.Model):
	number_of_injury=models.CharField(max_length=1000,blank=True)
	number_of_death=models.CharField(max_length=1000,blank=True)
	number_of_damage_vehicle=models.CharField(max_length=1000,blank=True)

