from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    
    name = models.fields.CharField(max_length=20)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=False)
    official_homepage = models.fields.URLField(max_length=100)

class Listing(models.Model):

    class types(models.Choices):
        Records = 'RCD'
        Clothing = 'CTG'
        Posters = 'PRS'
        Miscellaneous = 'MCL'

    name = models.fields.CharField(max_length=30)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(blank=True,null=True)
    type = models.fields.CharField(choices=types.choices)