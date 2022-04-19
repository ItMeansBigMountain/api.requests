import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#GETS OUR WEBPAGE OPENED UP
page = requests.get('https://www.hockey-reference.com/teams/CHI/2020_games.html')

#ALL OF THE HTML ON THE WEBSITE
soup = BeautifulSoup(page.content, 'html.parser')

#IDENTIFY THE BOX WITH ALL OF THE GAMES
allGames = soup.find(id="all_games")

#STATS [PARALLEL LISTS]
gameOutcome_list = [td.getText() for td in allGames.findAll('td', {'data-stat': "game_outcome"})]

opp_list = [td.getText() for td in allGames.findAll('td', {'data-stat': "opp_name"})]

#print(gameOutcome_list)
#print(opp_list)

win = 0
loss = 0
for game in gameOutcome_list:
  if game == "W":
    win = win + 1
  if game == "L":
    loss = loss + 1

print("WINS: ", win)
print("LOSS: " , loss)



# Pie chart
labels = 'Wins', 'Losses'
sizes = [win, loss]
explode = (0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()



#DIV means HTML box

#Parallel Lists are two lists🤡🤡🤡 [boxes] that will correspond 




