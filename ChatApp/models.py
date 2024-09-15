from django.db import models

class signup(models.Model):
    Firstname=models.CharField(max_length=20,default="")
    Lastname=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=20,default="")
    Password=models.CharField(max_length=20,default="")
    
class MiningActivity(models.Model):
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    excavation = models.FloatField()  # Volume of excavation (e.g., in tons)
    fuel_usage = models.FloatField()  # Fuel usage (e.g., in liters)
    machinery_details = models.TextField()  # Details of machinery

class CarbonSink(models.Model):
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    forest_area = models.FloatField()  # Forest area (in hectares)
    tree_count = models.IntegerField()  # Number of trees
    carbon_capture_tech = models.CharField(max_length=255)  # Other carbon capture methods

class EmissionCalculation(models.Model):
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    total_emissions = models.FloatField()  # Total calculated emissions
    total_absorption = models.FloatField()  # Total carbon absorption
    gap = models.FloatField()  # Emissions - Absorption
