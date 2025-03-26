from django.db import models

class City(models.Model):  # Changed 'city' to 'City'
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


'''
from django.db import models

class City(models.Model):
    """
    Model representing a city.
    
    Attributes:
        name (CharField): The name of the city (max length 25 characters).
    """
    name = models.CharField(max_length=25, unique=True, verbose_name="City Name")

    def __str__(self):
        """String representation of the City model"""
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'  # Correct plural form in admin interface
        ordering = ['name']  # Default ordering by city name
        db_table = 'cities'  # Optional: custom database table name

'''
        
        
'''
**Project: Weather Forecast App**
🔹 Built a Django web application that fetches real-time weather data using OpenWeatherMap API.
🔹 Users can search for any city to view temperature, humidity, wind speed, and a 5-day forecast.
🔹 Implemented an interactive UI using Bootstrap for a responsive design.
🔹 Used Django views and templates to dynamically display weather data.
🔹 Hosted the app on Heroku/Render for live access.


'''