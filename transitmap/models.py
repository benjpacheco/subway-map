# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SubwayMap(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    subwayline = models.CharField(max_length=17, blank=True, null=True)
    stationname = models.CharField(max_length=39, blank=True, null=True)
    route1 = models.CharField(max_length=2, blank=True, null=True)
    route2 = models.CharField(max_length=2, blank=True, null=True)
    route3 = models.CharField(max_length=2, blank=True, null=True)
    route4 = models.CharField(max_length=2, blank=True, null=True)
    route5 = models.CharField(max_length=2, blank=True, null=True)
    route6 = models.CharField(max_length=2, blank=True, null=True)
    route7 = models.CharField(max_length=2, blank=True, null=True)
    route8 = models.CharField(max_length=2, blank=True, null=True)
    route9 = models.CharField(max_length=2, blank=True, null=True)
    route10 = models.CharField(max_length=2, blank=True, null=True)
    route11 = models.CharField(max_length=2, blank=True, null=True)
    entrancetype = models.CharField(max_length=13, blank=True, null=True)
    entry = models.BooleanField(blank=True, null=True)
    ada = models.BooleanField(blank=True, null=True)
    freecrossover = models.BooleanField(blank=True, null=True)
    entrancelat = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    entrancelong = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)

    class Meta:
        db_table = 'subway'

    def __str__(self):
        return self.id