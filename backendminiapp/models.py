from django.db import models

# Create your models here.
from django.db import models

class Legislator(models.Model):
	PARTY_CHOICES = (("D","Democrat")("R","Republican")("I","Independant"))

    in_office = models.BooleanField()
    party = models.CharField(max_length=1,choices=PARTY_CHOICES)
    gender = models.Charfeild(max_length=3, )
    state = models.CharField(max_length=3)
    state_name = models.CharField(max_length=3)
    district = models.CharField(max_length=3)
    title = models.CharField(max_length=3)
    chamber = models.CharField(max_length=42)
    senate_class = models.CharField(max_length=42)
    state_rank = models.CharField(max_length=42)
    birthday = models.DateField()
    term_start = models.DateField()
    term_end = models.DateField()

