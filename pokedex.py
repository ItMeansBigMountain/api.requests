import requests 
import json
import pprint

pokemon = input("Please enter a pokemon that you wanna look up!: ")

pokedex_call = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon).json()

print()
for key , value in pokedex_call.items():
	print(key)
print()

option = input('please enter a query: ')
print()


#cleaning data
if option == 'moves':
  for x in pokedex_call[option]:
    print(x['move']['name'])

	
elif option == 'stats':
  for x in pokedex_call[option]:
    print(str(x['stat']['name']) ,'--', str(x['base_stat']) )
		
elif option =="abilities":
  for x in pokedex_call[option]:
    print(x["ability"]["name"])

    ability_desc = requests.get(x["ability"]["url"]).json()

    print(ability_desc['effect_entries'][1]["effect"])
    print()







else:
	print(pokedex_call[option])
