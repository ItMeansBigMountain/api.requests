import requests #lets us request a http response
import json #convert response strings into progromatic data
import pprint

# Request = requests.get('http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3')

def fetchRecipies(ingredients , searchQ ):
    url = "http://www.recipepuppy.com/api/?i="

    try:
        stop = int(input("How many pages do you wanna limit?: "))
    except:
        stop = float("inf")

    page = 1
    url+= ingredients + "&q=" + searchQ   +"&p="+ str(page)
    worthwhile = True
    while worthwhile:
        if page > stop:
            break
        else:
            #access api
            Request = requests.get(url + str(page))
            #cleaned data
            RecipiePayload = json.loads(Request.text)
            results =  RecipiePayload["results"]
            if results == []:
                break
            else:
                for x in results: # ACCESSING ALL RECIPIES ON PAGE! 
                    print()
                    print(x["title"])
                    print(x["href"])
                    print(x["ingredients"])
                    print()
                page += 1
                print("Page: " + str(page))


print('Welcome! Lets look up a recipie. ')
ingredients = input("Please enter ingredients\nSeperate each with commas: ")
searchQ = input("Please Enter Any Keyword : ")
fetchRecipies(ingredients , searchQ )



