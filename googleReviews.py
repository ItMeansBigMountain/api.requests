import requests
import json
import re
import datetime

from pprint import pprint




'''
PROCEDURE
    search google maps for those businesses
    fetch reviews
    read reviews and look for name or dates of employment
    return relative data


# API REVIEWS
# ['user', 'rating', 'date', 'summary', 'snippet', 'response']


'''




# user personal info
name = input("Please enter your name: ").lower()

# employment date
recruitment_year = int(input('Enter emplyment year: '))
employment_date = datetime.date(recruitment_year, 1, 1)

# termination date
still_employed = True
current_date = datetime.datetime.now()
employed_input = input("Are you still employed? y/n: ").lower()
if employed_input.startswith("n"):
    still_employed = False
    termination_year = int(input('Enter termination year: '))

if still_employed:
    termination_date = datetime.datetime.now() 
else:
    termination_date = datetime.date(termination_year, 1, 1)







# user input to search google maps (business name and address)
search_q = input("Please input business name (caps is important): ")


# data init
api_key = ""
url = f"https://serpapi.com/search.json?engine=google_maps&q={search_q}&type=search&api_key={api_key}"



# fetch data
data = requests.get(url).json()


# # paginate all found listings NEEDS LOCATION LAT/LON
# all_listings = data['local_results']
# while "serpapi_pagination" in data:
#     data =  requests.get(data['serpapi_pagination']['next'] + f"&api_key={api_key}").json()
#     print(data)
#     print(len(all_listings))
#     all_listings.extend(data['local_results']) 



# menu
for item in range(0,len(data['local_results']),1):
    print( f"\n\n{item}:\t" ,data['local_results'][item]['title'])
    print(data['local_results'][item]['address'])



# user choice and validation
try:
    choice = int(input("Please Choose appropriate result: "))
except:
    print("\n\nERROR: PLEASE USE NUMBER INDEX NEXT TO TITLE OF BUSINESSES")
    choice = int(input("Please Choose appropriate result: "))



# specified business data
business = data['local_results'][choice]



# fetch reviews of selected business
reviews_url = f"{ business['reviews_link']}&api_key={api_key}"
reviews = requests.get( reviews_url ).json()




# paginate all found listings NEEDS LOCATION LAT/LON
all_reviews = reviews['reviews']
while reviews["serpapi_pagination"]['next_page_token'] != "":
    reviews =  requests.get(reviews['serpapi_pagination']['next'] + f"&api_key={api_key}").json()
    all_reviews.extend(reviews['reviews']) 




# SAVE ALL BUSINESS REVIEWS AS JSON
with open(f"{business['title']}_reviews.json" , "w" ) as f : 
    json.dump(all_reviews, f)





# RELEVANT DATA 
# TODO:
    # get time ranges with matches for conversational times
relevant_data = {
    "name" : [] ,
    "date" : [] ,
}

for x in range(0,len(all_reviews),1):
    # SEARCH each review 
    if "snippet" in all_reviews[x]:


        # DATE SEARCH
        time_ago_arr = all_reviews[x]['date'].split()
        review_date = None
        
        # within one year
        if time_ago_arr[1] in ['month', 'months', 'second', 'seconds', 'hour', 'hours']:
            review_date =  datetime.datetime(current_date.year, 1, 1)
        # one year
        elif time_ago_arr[1] == 'year':
            review_date = datetime.datetime(current_date.year-1, 1, 1)
        # multiple years
        else:
            review_date = datetime.datetime(current_date.year- int(time_ago_arr[0]) , 1, 1)


        # CHECK IF REVIEW DATE IS BETWEEN TERMINATION AND EMPLOYMENT DATE
        if review_date.year  <= termination_date.year and review_date.year  >= employment_date.year :
            relevant_data['date'].append(all_reviews[x])





        # NAME SEARCH
        # snippet = all_reviews[x]['snippet'].split()
        # # SEARCH each word
        # for word in range(0,len(snippet),1):
        #     # CHECK if word has 2 caps
        #     uppercaseSplit = re.findall('[A-Z][^A-Z]*', snippet[word] )
        #     if len(uppercaseSplit) > 1:
        #         snippet[word] = uppercaseSplit[1]
        #         # CHECK IF REMOVED WORD IS NAME!
        #         if uppercaseSplit[0].lower() == name: relevant_data['name'].append(all_reviews[x]);break
        #     # CHECK for name in review
        #     if snippet[word].lower() == name: relevant_data['name'].append(all_reviews[x]) ; break


        found_name = all_reviews[x]['snippet'].lower().find(name)
        if found_name:
            relevant_data['name'].append(all_reviews[x]['snippet'])







# OUTPUT
print("\nReviews within date" , len(relevant_data['date']))
print("Reviews with name mentioned" , len(relevant_data['name']))

# SAVE ALL RELEVANT REVIEWS AS JSON
with open(f"relevant_to_{name}.json" , "w" ) as f : 
    json.dump(relevant_data, f)
