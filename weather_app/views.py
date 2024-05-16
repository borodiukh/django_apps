from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CityForm
import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_weather_and_forecast(city, api_key):
    response = requests.get(f'https://api.weatherapi.com/v1/forecast.json?q={city}&days=7&hour=24&key={api_key}').json()

    if 'error' in response:
        if response['error']['code'] == 1006:
            return {'error': 'No matching location found.Please try again.'}
        # API key errors
        elif response['error']['code'] in [2008, 1002]:
            return {'error': 'API key is invalid or not provided.'}
        else:
            return {'error': 'Unknown error.'}

    weather_data = dict()
    try:
        weather_data['city'] = response['location']['name']
        weather_data['country'] = response['location']['country']
        weather_data['forecast'] = []

        counter = 0
        for day in response['forecast']['forecastday']:
            weather_data['forecast'].append({})
            weather_data['forecast'][counter]['date'] = day['date']
            weather_data['forecast'][counter]['min_temp'] = day['day']['mintemp_c']
            weather_data['forecast'][counter]['max_temp'] = day['day']['maxtemp_c']
            weather_data['forecast'][counter]['max_wind'] = day['day']['maxwind_kph']
            weather_data['forecast'][counter]['weather'] = day['day']['condition']['text']
            weather_data['forecast'][counter]['weather_icon'] = day['day']['condition']['icon']

            counter += 1
    except:
        return {'error': 'Unknown error.'}

    else:
        return weather_data


def index(request):
    if request.method == 'GET':
        form = CityForm()
        context = {'form': form}
        return render(request, 'weather_app/main.html', context=context)

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data.get('city')

            answer = fetch_weather_and_forecast(city_name, API_KEY)
            if 'error' in answer:
                messages.error(request, answer['error'])
                return redirect('/weather/')

            context = {'weather_data': answer}
            return render(request, 'weather_app/weather.html', context=context)


