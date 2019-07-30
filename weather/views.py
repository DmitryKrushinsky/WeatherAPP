from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):

    appid = 'd95b3dcbc250ef07cb3befbe6695e5e8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    allcities = []
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city' : city.name,
            'temp' : response['main']['temp'],
            'icon' : response['weather'][0]['icon'],
        }
        allcities.append(city_info) 
    context = {'all_info': allcities, 'form': form}
    return render(request, 'weather/index.html', context)
# Create your views here.