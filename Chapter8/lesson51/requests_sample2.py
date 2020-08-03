import requests

r = requests.get('https://connpass.com/api/v1/event/?keyword=Python,東京')
print(r.status_code)
print(r.text[:100])
