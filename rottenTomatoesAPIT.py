#DOCUMENTATION
# https://pypi.org/project/tmdbsimple/#:~:text=tmdbsimple%20is%20a%20wrapper%2C%20written,out%20the%20overview%20and%20documentation


import tmdbsimple as tmdb
import pprint

tmdb.API_KEY = ''
search = tmdb.Search()
userSearchInput = input("Please type in a movie to search: ")
response = search.movie(query= userSearchInput)
pprint.pprint(response)

for s in search.results:
  #printing parameters for each item in list (search results)
   print(s['title'])
   print("ID: ",s['id'])
   print("Release Date: ",s['release_date'])
   print("Popularity: ",s['popularity'])
   print()

#PARAMETERS
  # "title"
  # "id"
  # "release_date"
  # "popularity"
  # "overview"
  # "overview"
  # "overview"
  # "vote_count"


