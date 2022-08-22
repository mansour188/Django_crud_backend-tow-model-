from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Personne(models.Model):
    name=models.fields.CharField(max_length=100)
    age=models.fields.IntegerField()
    matr=models.fields.IntegerField()

class Band(models.Model):
    class Gener(models.TextChoices):
        Hiphop="HH"
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name=models.fields.CharField(max_length=20)

    genere=models.fields.CharField(max_length=5,choices=Gener.choices)
    bio=models.fields.CharField(max_length=10)
    year_formed=models.fields.IntegerField(null=True, blank=True,validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active=models.fields.BooleanField(default=True)
    ofecial_page=models.fields.URLField(null=True)
    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    class Types(models.TextChoices):
        Records="R"
        clothing="C"
        posters="P"
        miscellaneous="M"
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=100)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(null=True,validators=[MinValueValidator(1990),MaxValueValidator(2022)])
    type=models.fields.CharField(max_length=10,choices=Types.choices)
    band=models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f" {self.title}"



