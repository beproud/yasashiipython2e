import requests

r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
weather_data = r.json()

city = weather_data['location']['city']
telop = weather_data['forecasts'][0]['telop']
print(f'{city} {telop}')
