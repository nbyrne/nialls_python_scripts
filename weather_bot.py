import requests

api_key = "261a97f2227d77cb736b292239f7f7c6"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

    response = requests.get(api_url)
    response_dict = response.json()

    weather = response_dict["weather"][0]["description"]

    if response.status_code == 200:
        return weather
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None
        
weather = get_weather("Longmont")
print(weather)