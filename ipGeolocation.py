import requests #lets us request a http response
import json #convert response strings into progromatic data

# GET AUTH KEY FROM https://ipgeolocation.io/
api_key = ""

ipAddress = input('Please enter IP Address: ')

Request = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip='+ ipAddress +'&fields=city&output=json')

sample = json.loads(Request.text)

print(sample) #not free anymore

# print('Ip Address: {}'.format(sample['ip']))
# print('City: {}'.format(sample['city']))