import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CityForm
from .models import City  # Updated import
from django.urls import reverse_lazy
from decouple import config

def index(request):
    new_city, url, token_key = None, '', config('TOKEN_KEY', default='your_default_api_key')
    err_msg, message, message_class = '', '', ''
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            url = f'http://api.openweathermap.org/data/2.5/weather?q={new_city}&units=metric&appid={token_key}'
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url).json()
                if r.get('cod') == 200:
                    form.save()
                else:
                    err_msg = "City doesn't exist"
            else:
                err_msg = "City already exists in the database!"

        message, message_class = (err_msg, 'alert-danger') if err_msg else ('City added successfully!', 'alert-success')

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for citi in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={citi.name}&units=metric&appid={token_key}'
        r = requests.get(url).json()

        if r.get('cod') == 200:
            city_weather = {
                'city': citi.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'weather/weather.html', context)

def about(request):
    return render(request, 'weather/about.html')

def delete_city(request, city_name):
    City.objects.filter(name=city_name).delete()  # Safe delete
    return redirect('index')  # Ensure the correct view name

def help(request):
    return render(request, 'weather/help.html')

def delete_all(request):
    """View to delete all cities"""
    City.objects.all().delete()
    return redirect('home')


'''
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CityForm
from .models import City  # Fixed incorrect model name (should start with uppercase)
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from decouple import config


def index(request):
    new_city = None
    token_key = config('TOKEN_KEY', default='')
    err_msg, message, message_class = '', '', ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            url = f'http://api.openweathermap.org/data/2.5/weather?q={new_city}&units=metric&appid={token_key}'
            existing_city_count = City.objects.filter(name=new_city).count()  # Fixed model reference

            if existing_city_count == 0:
                r = requests.get(url).json()
                if r.get('cod') == 200:  # Using `.get()` to avoid KeyError
                    form.save()
                else:
                    err_msg = "City doesn't exist"
            else:
                err_msg = "City already exists in the database!"

        if err_msg:
            message = err_msg
            message_class = 'alert-danger'
        else:
            message = 'City added successfully!'
            message_class = "alert-success"

    form = CityForm()
    cities = City.objects.all()  # Fixed model reference

    weather_data = []

    for citi in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={citi.name}&units=metric&appid={token_key}'  # Fixed missing `.name`
        r = requests.get(url).json()
        
        if r.get('cod') == 200:  # Ensuring API response is valid
            city_weather = {
                'city': citi.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'weather/weather.html', context)


def about(request):
    return render(request, 'weather/about.html')


def delete_city(request, city_name):
    City.objects.filter(name=city_name).delete()  # Used `.filter().delete()` to avoid errors
    return redirect('home')


def help(request):
    return render(request, 'weather/help.html')




'''