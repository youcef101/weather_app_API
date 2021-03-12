from django.shortcuts import render,redirect
import requests
from .forms import CityForm
from .models import City

# Create your views here.
def weather(request):
    api_url='http://api.openweathermap.org/data/2.5/weather?appid=f3bef68b650ff7df85699eaef8d394d7&q='
    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=CityForm()
        
        
    cities=City.objects.all() 
    weather_data=[]
    if cities:
        for city in cities:   
               url=api_url + str(city)
               response=requests.get(url)
               content=response.json()
               city_weather = {
                 'city':city.title,
                 'temperature':content['main']['temp'],
                 'description':content['weather'][0]['description'],
                 'icon':content['weather'][0]['icon'],
               }
               weather_data.append(city_weather)
   
               context={'weather_data':weather_data,'city':city}
    return render(request,'app/weather.html',context)

def delete_item(request,id):
    citiy=City.objects.get(pk=id).delete()
    return redirect('/')