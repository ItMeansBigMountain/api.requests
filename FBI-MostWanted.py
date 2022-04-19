import requests
import json
import matplotlib.pyplot as plt
import pprint
import time


# response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'field_offices': 'chicago', 'page': 1})

# response = requests.get('https://api.fbi.gov/wanted/v1/list', params={ 'page': 45})


def piechart(labels , sizes):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def showAll(city):
    for page in range(1 , 100, 1 ):

        if city == "" or city == None:
            response = requests.get('https://api.fbi.gov/wanted/v1/list', params={ 'page': page})
        else:
            response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'field_offices': city, 'page': page})

        data = json.loads(response.content)
        items = data["items"]
        if items == []:
            break

        for x in items:
            print(x["title"])
            print(x["warning_message"])
            print(x["race"])
            print(x["weight"])
            print(x["caution"])
            print()


        print("Page: ", page)
        print()
        time.sleep(.5)
    print("Total Results: ", data["total"])

def raceCounter(city):

    none_names = []
    white_names = []
    native_names = []
    black_names = []
    hispanic_names = []
    asian_names = []


    for page in range(1 , 100, 1 ):
        
        if city == "" or city == None:
            response = requests.get('https://api.fbi.gov/wanted/v1/list', params={ 'page': page})
        else:
            response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'field_offices': city, 'page': page})

        data = json.loads(response.content)
        items = data["items"]
        if items == []:
            break

        for x in items:

            if x["race"] == '':
                none_names.append(x["title"])

            elif x["race"] == None:
                none_names.append(x["title"])

            elif x["race"] == 'white':
                white_names.append(x["title"])

            elif x["race"] == 'native':
                native_names.append(x["title"])

            elif x["race"] == 'black':
                black_names.append(x["title"])

            elif x["race"] == 'hispanic':
                hispanic_names.append(x["title"])

            elif x["race"] == 'asian':
                asian_names.append(x["title"])



        print("Page: ", page)


    print("NONE (normally Arabs & Persians)")
    print(none_names)
    print()

    print("White")
    print(white_names)
    print()

    print("Native American")
    print(native_names)
    print()

    print("Black")
    print(black_names)
    print()

    print("Hispanic")
    print(hispanic_names)
    print()

    print('Asian')
    print(asian_names)
    print()
    

    print(  "None: " ,  len(none_names))
    print(  "White: " ,  len(white_names))
    print(  "Native: " ,  len(native_names))
    print(  "Black: " ,  len(black_names))
    print(  "Hispanic: " ,  len(hispanic_names))
    print(  "Asian: " ,  len(asian_names))

    print("\nTotal Results: ", data["total"])




    labels = "NONE (normally Arabs & Persians)" , "White" , "Native" , "Black" , "Hispanic" , "Asian"

    sizes = [
        len(none_names) ,
        len(white_names) ,
        len(native_names) ,
        len(black_names) ,
        len(hispanic_names) ,
        len(asian_names)
    ]

    piechart(labels , sizes)

def main():

    print("Welcome to the FBI api")
    city = input("Please enter main city that you would like to look up, Leave blank for all [NO SPACES]: ")
    
    print("1: Show all data of every person on the list.")
    print("2: See the race count total with pie chart\n")
    option = input("Please choose an option: ")
    if option == "1":
        showAll(city)
    elif option == "2":
        raceCounter(city)

main()