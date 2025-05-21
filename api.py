import requests
import json
import time


from PIL import Image
import io
import matplotlib.pyplot as plt



def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&leng=es"
           #http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es
    response = requests.get(url)
    
    #print(response)
    print("\n ")
    return response.json()

api_key = "6901337217e11358a24cf97f028aafa9"
#city = "tokio"


while True:
    try:
          
        icon_to_emoji = {
            '01d': '☀️',  # Sol
            '01n': '🌙',  # Luna
            '02d': '⛅',  # Sol con nubes
            '02n': '🌙☁️',  # Luna con nubes
            '03d': '☁️',  # Nubes dispersas
            '03n': '🌙☁️',  # Nubes dispersas (noche)
            '04d': 'OVERCAST',  # Nubes rotas
            '04n': 'OVERCAST',  # Nubes rotas (noche)
            '09d': '🌧️',  # Lluvia ligera
            '09n': '🌧️',  # Lluvia ligera (noche)
            '10d': '🌦️',  # Lluvia
            '10n': '🌙🌧️',  # Lluvia (noche)
            '11d': '⚡',  # Tormenta
            '11n': '🌙⚡',  # Tormenta (noche)
            '13d': '❄️',  # Nieve
            '13n': '🌙❄️',  # Nieve (noche)
            '50d': '🌫️',  # Niebla
            '50n': '🌙🌫️',  # Niebla (noche)
        }
        city = input("\n\t Ingresar ciuad:  ")
        weather_data = get_weather(city, api_key)
        print(weather_data)
        weather_data_json = json.dumps(weather_data)
        print(weather_data_json)
        if weather_data:
            print("\t" + "-"*50 + "|")
            #print(f"\t  La ciudad es: {weather_data["name"]}\n\t  La temperatura es: {weather_data["main"]["temp"]}\n \t  Estado del clima: {weather_data["weather"][0]['main']} \n\t  Descripcion: {weather_data["weather"][0]["description"]}")
            print(f'''
                    \tLa ciudad es: {weather_data["name"]}\n
                    \tLa temperatura es: {weather_data["main"]["temp"]}\n 
                    \tEstado del clima: {weather_data["weather"][0]['main']}\n
                    \tDescripcion: {weather_data["weather"][0]["description"]}
                    ''')
        icon_code =  weather_data["weather"][0]['icon']
        print(icon_code)
        emojis= icon_url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'
        icon_response = requests.get(icon_url)
        if icon_response.status_code == 200:
                icon_image = Image.open(io.BytesIO(icon_response.content))
                plt.imshow(icon_image)
                plt.axis('off')  # Ocultar ejes
                plt.show()
    except: 
        print("error intente de nuevo ")






print("\n \n")
weather_data_json = json.dumps(weather_data)
print(weather_data_json)
print("\n \n") 


# weater_data = {'coord': {'lon': 2.159, 'lat': 41.3888}, 
#                'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
#                'base': 'stations', 'main':
#                                             {'temp': 22.84, 'feels_like': 22.62, 'temp_min': 22.05, 'temp_max': 25.13,
#                                             'pressure': 1013, 'humidity': 55, 'sea_level': 1013, 'grnd_level': 1005},
#                                             'visibility': 10000, 
#                                             'wind': {'speed': 1.79, 'deg': 210, 'gust': 3.58},
#                                             'clouds': {'all': 100}, 
#                                             'dt': 1747308622, 
#                                             'sys': {'type': 2, 'id': 2032131,'country': 'ES', 'sunrise': 1747283556, 'sunset': 1747335781}, 
#                                                     'timezone': 7200, 'id': 3128760, 'name': 'Barcelona', 'cod': 200}

# print("\n \n")
# print(weather_data)
# print("\n \n")
# print(weather_data['main'])
# print("\n\n")
# print(weather_data['sys'])
# print("\n\n")
# print(weather_data['sys']['country'])
# print("\n\n")
# print(weather_data['name'])
#print(weater_data['country'])

#contry,
#humidity: 
# name : 

