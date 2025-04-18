from dotenv import load_dotenv
import os #библиотека операционной системы
import requests # библиотека чтобы делать запросы


load_dotenv()  #загрузить секретные ключи

API_KEY="9b9938037465439bbf9174353251004"
API_URL="http://api.weatherapi.com/v1/forecast.json"
#API_KEY = os.getenv("API_KEY")
#API_URL = os.getenv("API_URL")
DAYS = 1  #загрузить дни 
LANG = 'ru' #выбрать язык
AQI='yes'

'''
response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': DAYS, 'lang': LANG}) #все данные придут в response
data = response.json()
'''

'''
for h in data:
    print(h)
print("")
for h in data["forecast"]["forecastday"][0]:
    print(h)
print("")
for h in data["forecast"]["forecastday"][0]["day"]:
    print(h)
print("")

#print(data)

print("location")
for key, value in data["location"].items():
    print(f"{key}:    {value}")
print("")
print("current")
for key, value in data["current"].items():
    print(f"{key}:    {value}")
print("")
print("forecast")
for key, value in data["forecast"].items():
    print(f"{key}:    {value}")
    print("")



for h in data["forecast"]:
 #   print(h["time"][-5:])
    print(h)
 #   print(data[h])
    print("")
print(data["current"])
'''

'''
location = data['location']
forecast_hours = data['forecast']['forecastday'][0]['hour']
city_name = location['name']
country_name = location['country']
time = location['localtime']
current = data['current']

#hours=[h['time'][-5:] for h in forecast_hours]
hours=[h for h in forecast_hours]

print(location)
print("")
#print(forecast_hours)
for h in forecast_hours:
    print(h["time"][-5:])
    print(h)
    print("")
#print(hours)
print("")
print(country_name, '  ', city_name, '  ', time[0:10], '   ',time[11:16] )
#print(current)
'''

def load_data(city):

    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': DAYS, 'lang': LANG, 'aqi': AQI}) #все данные придут в response
    data = response.json()


    location = data['location']
    forecast_hours = data['forecast']['forecastday'][0]['hour']
    city_name = location['name']
    current = data['current']
    icon = current['condition']['icon']
    condition = current['condition']['text']
    temp = current['temp_c']
    
    hours = [h['time'][-5:] for h in forecast_hours]
  #  temps = [h['temp_c'] for h in forecast_hours]
  #  ap = [h['pressure_mb'] for h in forecast_hours]
  #  humidity = [h['humidity'] for h in forecast_hours]
  #  wind = [h['wind_kph'] for h in forecast_hours]
  #  wind_dirs = [h['wind_degree'] for h in forecast_hours]
    

    date= [h["time"][0:10] for h in forecast_hours][0]
    co= [h["air_quality"]["co"] for h in forecast_hours]
    no2= [h["air_quality"]["no2"] for h in forecast_hours]
    o3= [h["air_quality"]["o3"] for h in forecast_hours]
    so2= [h["air_quality"]["so2"] for h in forecast_hours]
    pm2_5= [h["air_quality"]["pm2_5"] for h in forecast_hours]
    pm10= [h["air_quality"]["pm10"] for h in forecast_hours]


    return {"location": location,
            "city_name": city_name,
            "icon": icon,
            "temp": temp,
            "hours": hours,
          #  "temps": temps,
          #  "ap": ap,
          #  "humidity": humidity,
          #  "wind": wind,
          #  "wind_dirs": wind_dirs,
            "condition": condition,           
            "date": date,
            "co": co,
            "no2": no2,
            "o3": o3, 
            "so2": so2,
            "pm2_5": pm2_5,
            "pm10": pm10}
        