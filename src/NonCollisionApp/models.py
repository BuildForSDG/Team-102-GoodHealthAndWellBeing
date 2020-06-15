from django.db import models

# Create your models here.

class ResponseDetails(models.Model):

    type_choices = (
        ('1', 'Cultism'),
        ('2', 'Kidnapppers'),
        ('3', 'Arm Robbers station'),
        ('4', 'Area Boys'),
        ('5', 'Banditry'),
        ('6', 'Hilly area'),
        ('7', 'Others'),
    )

    # Fields

    Incident_happening = models.CharField(max_length=20, choices=type_choices,
                                          default='')
    State = models.CharField(max_length=20, default='')
    LG_Area = models.CharField(max_length=100, default='')
    Along_the_Way = models.TextField(max_length=100, default='', blank=True)
    Description_Of_the_Area = models.TextField(default='')
    Photo_of_Area = models.ImageField(upload_to="images/", default='scan')


def __str__(self):
    return self.Incident_happening

class State(models.Model):
    #    Model definition for State.
    name = models.CharField(max_length=45, null=True, blank=True)
    capital = models.CharField(max_length=45, null=True, blank=True)
    zone = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        #    Meta definition for State.

        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        #    Unicode representation of State.
        return self.name


class LGA(models.Model):
    # Model definition for LGA.

    name = models.CharField(max_length=150, null=True, blank=True)
    state = models.ForeignKey(State, related_name="lgas", on_delete=models.CASCADE)

    class Meta:
        # Meta definition for LGA.

        verbose_name = 'LGA'
        verbose_name_plural = 'LGAs'

    def __str__(self):
        # Unicode representation of LGA.
        return f"{self.name}|{self.state.name}"
