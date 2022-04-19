import http.client
import json
import pprint

import matplotlib.pyplot as plt

def main():
    #api setup
    conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    #input country
    country = input("Please enter country to look up ex: USA   : ")

    endprogram = False
    while endprogram == False:


        #options
        print("1: Today's statistics for country")
        print("2: Historical statistics for country")
        
        option = input("Please choose an option: ")

        if option == "1":
            getCountryStats(conn, headers, country)

        elif option == "2":
            getCountryHistory(conn, headers, country)

        elif option == "end" or option == None:
            endprogram = True
            break
        else:
            print("ERROR: INVALID INPUT\n RESETTING APPLICATION\n")
            break

def getCountryStats(conn, headers, country):
    conn.request("GET", "/statistics?country="+country, headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    read = json.loads(data)
    response = read["response"][0]


    date = response["day"]
    country = response["country"]
    population = response["population"]
    cases = response["cases"]
    deaths = response["deaths"]
    tests = response["tests"]


    pprint.pprint(response)


    print("\n1M_pop mean 'total confirmed cases per 1 million population'")

def getCountryHistory(conn, headers, country):
    conn.request("GET", "/history?country=" + country, headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    read = json.loads(data)

    response = read["response"]


    def criticalOutOfActive():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                active = cases["active"]
                critical = cases["critical"]
                

                xbox.append(day)
                ybox.append( critical / active)

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Critical Out Of Active Cases", color)
        print(xbox)

    def DeathOverInfection():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                total_cases = cases["total"]
                
                deaths = response[x]['deaths']["total"] #int/float

                xbox.append(day)
                ybox.append( deaths / total_cases)

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Deaths Out Of Total Cases", color)

    def TotalOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                total_cases = cases["total"]

                xbox.append(day)
                ybox.append( total_cases)

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Total Cases Over Time", color)

    def TotalDeathsOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                deaths = response[x]['deaths']["total"] #int/float

                xbox.append(day)
                ybox.append( deaths)

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Accumilated Deaths", color)

    def NewCasesOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                new = cases["new"]

                xbox.append(day)
                ybox.append( int(new))

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "New Cases Over Time", color)

    def ActiveCasesOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                active = cases["active"]

                xbox.append(day)
                ybox.append( int(active))

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Active Cases Over Time", color)

    def RecoveryOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                recovered = cases["recovered"]

                xbox.append(day)
                ybox.append( int(recovered))

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Recovery Over Time", color)

    def NewlyInfectedMinusNewlyRecoveredOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                new = cases["new"]
                recovered = cases["recovered"]

                xbox.append(day)
                ybox.append( int(new) - int(recovered))

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "New cases in & Recovered cases out", color)

    def CriticalCasesOverTime():

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                critical = cases["critical"]

                xbox.append(day)
                ybox.append( critical)

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "Critical Conditions Over Time", color)

    def NewDeathsOverTime(): # THIS FUNCTION HOLDS ALL DICT. DATAFIELDS STORED AS VARIABLES

        #build barchart for recover over admit
        xbox = []
        ybox = []
        for x in range(len(response) - 1  , 0 , -1):
            if response[x]['day'] == response[x-1]['day']:
                continue
            else:
                #defining data
                day = response[x]["day"]

                cases = response[x]['cases'] #dict
                active = cases["active"]
                critical = cases["critical"]
                new = cases["new"]
                recovered = cases["recovered"]
                total_cases = cases["total"]
                
                deaths = response[x]['deaths']["total"] #int/float
                NewDeaths = response[x]['deaths']["new"] #int/float

                xbox.append(day)
                ybox.append( int(NewDeaths))

                if max(ybox) > 1:
                    color = "green"
                else:
                    color = "red"
        bar_chart(  xbox , ybox , "x" , "y" , "New Deaths Over Time", color)



    # TODO LIST
    #make menue to choose functions
    #edit functions to not make as many variables as well as reverse the iterations. also run it past someone smart so we can make better charts...


    #options
    print("\n\nBAR CHARTS ")
    print("\n1: Critical Out Of Active Cases ")
    print("2: Deaths Out Of Total Cases ")
    print("3: Total Cases Over Time ")
    print("4: Accumilated Deaths ")
    print("5: New Cases Over Time ")
    print("6: Active Cases Over Time ")
    print("7: Recovery Over Time ")
    print("8: New cases in & Recovered cases out ")
    print("9: Critical Conditions Over Time ")
    print("10: New Deaths Over Time \n")
    option = input("Please choose an option: ")

    if option == "1":
        criticalOutOfActive()
    
    elif option == "2":
        DeathOverInfection()
    
    elif option == "3":
        TotalOverTime()
    
    elif option == "4":
        TotalDeathsOverTime()
    
    elif option == "5":
        NewCasesOverTime()
    
    elif option == "6":
         ActiveCasesOverTime()
    
    elif option == "7":
        RecoveryOverTime()
    
    elif option == "8":
        NewlyInfectedMinusNewlyRecoveredOverTime()
    
    elif option == "9":
        CriticalCasesOverTime()
    
    elif option == "10":
        NewDeathsOverTime()

    else:
        print("ERROR: INVALID INPUT\n RESETTING APPLICATION\n")
        main()




    # criticalOutOfActive()
    # DeathOverInfection()
    # TotalOverTime()
    # TotalDeathsOverTime()
    # NewCasesOverTime()
    # ActiveCasesOverTime()
    # RecoveryOverTime()
    # NewlyInfectedMinusNewlyRecoveredOverTime()
    # CriticalCasesOverTime()
    # NewDeathsOverTime()


    # pprint.pprint(response)
    

def bar_chart(x , y , X_label , Y_label, Title , color_input):
    plt.style.use('ggplot')
    # x = []
    # y = []
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, y, color= color_input ) #STR ex: "green"
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.xticks(x_pos, x)
    plt.show()
# bar_chart([0,1,2,3] , [9,8,7,6] , "x" , "y" , "random")


main()