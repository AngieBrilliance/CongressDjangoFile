from django.db import models

"""These are the models. Models are lnes of code that represent Data being stored in
the database of the django file"""

class Legislator(models.Model):
	PARTY_CHOICES = (("D","Democrat",), ("R","Republican",), ("I","Independant"), )
	in_office = models.BooleanField()
	party = models.CharField(max_length=1,choices=PARTY_CHOICES)
	gender = models.CharField(max_length=3, )
	state = models.CharField(max_length=3)
	state_name = models.CharField(max_length=42)
	district = models.CharField(max_length=3)
	title = models.CharField(max_length=3)
	chamber = models.CharField(max_length=42)
	senate_class = models.CharField(max_length=42)
	state_rank = models.CharField(max_length=42)
	birthday = models.DateField()
	term_start = models.DateField()
	term_end = models.DateField()

	def __unicode__(self):
		return u"%s, %s" % (self.district, self.state_name, )
