import requests


# get token from here https://aqicn.org/data-platform/token/#/
token = ''


city = input("Please enter city name ex: 'chicago' \n > ")
url = f'https://api.waqi.info/feed/{city}/?token={token}'



data = requests.get(url).json()
print(data)