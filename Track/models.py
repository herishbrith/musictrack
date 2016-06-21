from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):

	genreId = models.AutoField(primary_key=True)
	genreName = models.CharField(max_length=20, unique=True)

	def __unicode__(self):

		return self.genreName


class Track(models.Model):

	trackId = models.AutoField(primary_key=True)
	trackTitle = models.CharField(max_length=20, unique=True)
	trackRating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
	trackGenre = models.ForeignKey(Genre)

	def __unicode__(self):

		return self.trackTitle




