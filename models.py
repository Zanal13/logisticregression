from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=255)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class City1(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    