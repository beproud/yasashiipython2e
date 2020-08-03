import requests

r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
r = requests.get('https://connpass.com/api/v1/event/?keyword=Python,東京')
print(r.status_code) # 200(正常終了を表すステータスコード)が表示される
print(r.text[:100]) # レスポンスの先頭100文字が表示される

weather_data = r.json()

city = weather_data['location']['city']
telop = weather_data['forecasts'][0]['telop']
print(f'{city} {telop}')
