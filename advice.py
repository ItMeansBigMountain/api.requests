#import modules that give us more functions
import requests 
import json

#access the api
Advice = requests.get("https://api.adviceslip.com/advice")


#convert api string into dictionary so that we can parse through it
Advice_dictionary = json.loads(Advice.text)


#fully parsed, clean data
api_id = Advice_dictionary["slip"]["id"]
api_advice = Advice_dictionary["slip"]["advice"]

print(api_id)
print(api_advice)

#printing dictionary that we can parse through
print()
print(Advice_dictionary)


#DICTIONARY PRACTICE
# dictionary = {
#   #KEY         VALUE
#   "teacher" : "affan" , 
#   "student" : "Quentin"
# }


# print(dictionary["student"])
