import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2888e164d095fe5f1385ff7ac8b97414'
    s=0
    form=CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        s=form.data['name']
        s=s.upper()

        
        if (City.objects.filter(name__iexact=s).count()) >0:
            form=CityForm()
        else:
            form.save()
             
    else:  
       
        form=CityForm()  

    cities = City.objects.filter(name__iexact=s)[:1]

    weather_data = []
    message_data=[]
  
    for city in cities:

        r = requests.get(url.format(city)).json()
        if r == {'cod':'404','message':'city not found'}:
            Message={
                'message':r['message']
            }
            message_data.append(Message)
          
        else:
            city_weather = {

                'city' : city.name,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
            

            weather_data.append(city_weather)

           
    return render(request, 'weather/weather.html', {'message_data':message_data,'weather_data':weather_data,'form':form})
