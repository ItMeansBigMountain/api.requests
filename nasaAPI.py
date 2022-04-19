import json
import requests
import datetime
from pprint import pprint
import random
import time

# images
from PIL import Image
from urllib.request import urlopen
import io
import pygame as pg

apiKey = ''

def timeLapse(latitude , longitude , SubDate , howmanyYears  ): # under construction 
    minuserYear = SubDate.year
    sampleUrl = []

    callDate = str(SubDate.date())[:10]
    for x in range(0 , howmanyYears , 1): # call the api for each year and grab a pic url
        latitudeLongitude = 'https://api.nasa.gov/planetary/earth/assets?lon='+longitude+'&lat='+latitude+'&date='+   callDate  +'&&dim=0.10&api_key=' + apiKey
        Request = requests.get(latitudeLongitude)
        sample = json.loads(Request.text)

        try: # check if there was a pic
            sampleUrl.append((sample['url'] , callDate))
        except Exception as e:
            pass

        #subtract one from the year
        minuserYear = minuserYear - 1
        callDate = str(minuserYear) + str(SubDate)[4:10]

    displayTimeLapse(sampleUrl)
    print('Displaying images...')

def displayTimeLapse(imgURLs):
    pg.init()
    screen = pg.display.set_mode((1500,1500),  pg.RESIZABLE )
    screen.fill((0, 0, 0))

    # go through the pics ---> sampleUrl = ( url , date )
    for i in range( len(imgURLs) ):
        pictureUrl = imgURLs[i][0] 
        print(pictureUrl)

        image_str = urlopen(pictureUrl).read()
        image_file = io.BytesIO(image_str)

        image = pg.image.load(image_file)
        screen.blit(image, (0, 0))

        pg.display.flip()
        time.sleep(5)

def hubblePics():
    hubbleCall = 'https://hubblesite.org/resource-gallery/images'
    Request = requests.get(hubbleCall)
    # sample = json.loads(Request.text)
    print(Request.text)

def ExoPlanet():
    exoCall = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname&format=json'
    Request = requests.get(exoCall)
    sample = json.loads(Request.text)
    
    howmany = len(sample) 
    kepler = 0

    for x  in sample:
        print(x['pl_hostname'])
        if 'Kepler' in  x['pl_hostname']:
            kepler = kepler + 1
    print("There are {} confirmed Exo Planets".format(howmany)  )
    print(kepler)

def marsRoverPics():


    
    marsRover = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=' + apiKey




    Request = requests.get(marsRover)
    sample = json.loads(Request.text)

    for x  in sample['photos']:
        imageSRC  = x['img_src']
        EarthDate = x['earth_date']
        camera = x['camera']['full_name']
        rover = x['rover']['name']
        roverLandingDate = x['rover']['landing_date']
        roverLaunchDate = x['rover']['launch_date']
        roverStatus = x['rover']['status']


        print(imageSRC)
        print(EarthDate)
        print(camera)
        print(rover)
        print(roverLandingDate)
        print(roverLaunchDate)
        print(roverStatus)
        print()

    print("There are {} pictures from Mars".format(  len(sample['photos'])  )  )
def randomPicFromMarz():
    marsRover = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=' + apiKey
    Request = requests.get(marsRover)
    sample = json.loads(Request.text)

    randomIndex = random.randint(0 , (len(sample) -1))

    randomPic = sample['photos'][randomIndex]
    
    imageSRC  = randomPic['img_src']
    EarthDate = randomPic['earth_date']
    camera = randomPic['camera']['full_name']
    rover = randomPic['rover']['name']
    roverLandingDate = randomPic['rover']['landing_date']
    roverLaunchDate = randomPic['rover']['launch_date']
    roverStatus = randomPic['rover']['status']

    print(imageSRC)
    print(EarthDate)
    print(camera)
    print(rover)
    print(roverLandingDate)
    print(roverLaunchDate)
    print(roverStatus)
    print()

def picturesfromNASA():
    searchQ = input("Please enter a search query: ")
    pictureCall = 'https://images-api.nasa.gov/search?q='  + searchQ
    # pictureCall = 'https://images-api.nasa.gov/search?year_start=2020'
    Request = requests.get(pictureCall)
    sample = json.loads(Request.text)


    for x in sample['collection']['items']:

        try:
            PictureLink = [i['href'] for i in x['links'] ]
        except Exception as e:
            print('--------------------------------------------')
            print(e)
            print('--------------------------------------------')

        for y in x['data']:
            media_type = y['media_type']
            description = y['description']
            title = y['title']
            dateCreated = y['date_created']

            print(title)
            print(dateCreated)
            print(PictureLink)
            print(media_type)
            # print(description)
            print()

def randomNASApic():
    searchQ = input("Please enter a search query: ")

    pictureCall = 'https://images-api.nasa.gov/search?q='+ searchQ
    Request = requests.get(pictureCall)
    sample = json.loads(Request.text)

    # print(sample)
    Container = []
    for x in sample['collection']['items']  :
        PictureLinks = [i['href'] for i in x['links'] ]
        Container.append(PictureLinks)
    print(  Container[random.randint(0,len(Container)-1)]  )

def marsWeather():
    marsWeather = 'https://api.nasa.gov/insight_weather/?api_key='+ apiKey+ '&feedtype=json&ver=1.0' 
    Request = requests.get(marsWeather)
    sample = json.loads(Request.text)

    avgLast7Days = 0 #average temp last 7 days
    for x in sample['sol_keys']:
        avgLast7Days += sample[x]['PRE']['av']
    avgLast7Days = avgLast7Days / len(sample['sol_keys'])

    todayMarsTemp = sample['sol_keys'][-1]

    avgTemp = sample[todayMarsTemp]['PRE']['av']
    month = sample[todayMarsTemp]['Month_ordinal']
    First_UTC = sample[todayMarsTemp]['First_UTC']
    Last_UTC = sample[todayMarsTemp]['Last_UTC']
    season = sample[todayMarsTemp]['Season']

    print('Average Last 7 Days: {}\n'.format(avgLast7Days))
    print(avgTemp)
    print(month)
    print(First_UTC)
    print(Last_UTC)
    print(season)

def main():
    today = datetime.datetime.today()
    print(today.date())
    print('Welcome to space')
    print("1 - randomNASApic")
    print("2 - picturesfromNASA")
    print("3 - marsWeather")
    print("4 - marsRoverPics")
    print("5 - randomPicFromMarz")
    print("6 - Exo Planet")
    print("7 - hubblePics")
    print("8 - timeLapse")

    option = input('Please choose an option: ')
    

    if option == '1':
        randomNASApic()


    elif option == '2':
        picturesfromNASA()


    elif option == '3':
        marsWeather()


    elif option == '4':
        marsRoverPics()


    elif option == '5':
        randomPicFromMarz()


    elif option == '6':
        ExoPlanet()


    elif option == '7':
        hubblePics()


    elif option == '8':
        latz = input("Please enter a latitude: ")
        longz = input("Please enter a longitude: ")
        howmanyYears = int(input("How many years would you like to go back?: "))
        timeLapse( latz  ,  longz , today , howmanyYears)



while True:
    main()
    opt = input("\n\n\n   - Press Enter to reset app \n   - type quit to exit ")
    if opt.lower().startswith("q"):
        print("Goodbye!")
        break
