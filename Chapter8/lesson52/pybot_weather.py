import requests

def weather_command():
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    city_code = '130010'
    url = f'{base_url}?city={city_code}'
    r = requests.get(url)
    weather_data = r.json()
    city = weather_data['location']['city']
    label = weather_data['forecasts'][0]['dateLabel']
    telop = weather_data['forecasts'][0]['telop']
    
    response = f'{city}ノ{label}ノ天気ハ「{telop}」デス'
    return response
