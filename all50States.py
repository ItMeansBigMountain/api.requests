import requests

website = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest"

data = requests.get(website).json()

list_of_states = data['data']


# output

print( )

for i in range(0, len(  list_of_states  ) , 1):
  print(  list_of_states[i]["State"] , list_of_states[i]["Population"]    )  




