import requests #lets us request a http response
import json #convert response strings into progromatic data
import pprint


#access api
Request = requests.get('https://api.tronalddump.io/random/quote')

#cleaned data
RequestTextDictionary = json.loads(Request.text)

quote = RequestTextDictionary["value"]

print(quote)


# pprint.pprint(RequestTextDictionary)
# for key , value in RequestTextDictionary.items():
#     print(key)
#     print(value)
#     print()



