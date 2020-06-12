from enum import unique

from django.db import models

# Create Your models here.

class State(models.Model):
#    Model definition for State.
    name = models.CharField(max_length=45,null=True,blank=True)
    capital = models.CharField(max_length=45,null=True,blank=True)
    zone = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
    #    Meta definition for State.

        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
    #    Unicode representation of State.
        return self.name

class LGA(models.Model):
    # Model definition for LGA.

    name = models.CharField(max_length=150,null=True,blank=True)
    state = models.ForeignKey(State, related_name="lgas", on_delete=models.CASCADE)

    class Meta:
    # Meta definition for LGA.

        verbose_name = 'LGA'
        verbose_name_plural = 'LGAs'

    def __str__(self):
	# Unicode representation of LGA.
        return f"{self.name}|{self.state.name}"
    
class PoliceStation(models.Model):
    division = models.CharField(max_length=45,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=45,null=True,blank=True)
    state = models.ForeignKey(State, related_name="stations",null=True, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, related_name="stations",null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.division}|{self.lga}"

    class Meta:
        managed = True
        verbose_name = 'PoliceStation'
        verbose_name_plural = 'PoliceStations'
        
class FRSC(models.Model):
    command = models.CharField(max_length=45,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=45,unique=True,blank=True)
    phone = models.CharField(max_length=45,null=True,blank=True)
    state = models.ForeignKey(State, related_name="road_safety",null=True, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, related_name="road_safety",null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.command}|{self.lga}"

    class Meta:
        managed = True
        verbose_name = 'FRSC'
        verbose_name_plural = 'FRSC'
        
class Hospital(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    type = models.CharField(max_length=45,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=45,unique=True,blank=True)
    phone = models.CharField(max_length=45,null=True,blank=True)
    mortuary = models.CharField(max_length=45,null=True,blank=True)
    state = models.ForeignKey(State, related_name="hospital",null=True, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, related_name="hospital",null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}|{self.lga}"

    class Meta:
        managed = True
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'
        
class Hotel(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=45,unique=True,blank=True)
    phone = models.CharField(max_length=45,null=True,blank=True)
    state = models.ForeignKey(State, related_name="hospitality",null=True, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, related_name="hospitality",null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}|{self.lga}"

    class Meta:
        managed = True
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
