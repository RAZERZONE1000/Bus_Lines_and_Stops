from django.db import models
from django.urls import reverse




class Stajaliste(models.Model):
    naziv      = models.CharField(max_length=100)
    ulica      = models.CharField(max_length=100)
    geoSirina  = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    geoDuzina  = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    def __str__(self):
        return self.naziv
    
    def get_absolute_url(self):
        return '/autobuske_linije/stajalista/'
    
    def get_coordinates(self):
        if self.geoSirina != None and self.geoDuzina != None:
            return str(self.geoSirina) + ', ' + str(self.geoDuzina)
    
        


class Linija(models.Model):
    naziv       = models.CharField(max_length=200)
    opis        = models.CharField(max_length=500, blank=True, null=True)
    stajalista  = models.ManyToManyField(Stajaliste)
    
    def __str__(self):
        return self.naziv
    
    def get_absolute_url(self):
        return '/autobuske_linije/'   
    
    def get_stajalista(self):
        stajalistaList = []
        for i in self.stajalista.all():
            stajalistaList.append(str(i))
        return (', '.join(stajalistaList))
    
    def stajalistaList(self):
        stajalistaList = []
        for i in self.stajalista.all():
            stajalistaList.append(str(i))
        return stajalistaList