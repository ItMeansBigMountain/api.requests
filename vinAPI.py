import requests 
import json
import pprint




# AUTH API KEY DOCUMENTATION 
    # https://www.vinaudit.com/vehicle-specifications-api?gclid=CjwKCAjwu_mSBhAYEiwA5BBmf85EZbhyKkVLYKMOJevnZqUFQAGElFTEd2_EaB4O5JJxQeerGBXOkhoCXfkQAvD_BwE

    
apiKey = ''




# available selections "returns dictionary that you may later clean"
def get_available_selections(apiKey , vinNumber):
    call = requests.get('https://specifications.vinaudit.com/v3/selections?key=' + apiKey + '&list=year+make+model+trim&format=json').json()

    print(call);exit()
    

    set_list = []

    # print(call['selections']['years'])
    for x in call['selections']['years']:
       
    #    uncomment these to check parameters of dictionary
        # print(x)
        # print(x['makes'])

        print(x['name'])
        for y in x['makes']:
            print(y['name'])
            set_list.append(y['name'])

        print()
        print('---------------------------------------------------------------------------------')
        print()

    set_list = set(set_list)
    print('\n\nALL AVAILABLE CARS ({} Brands)'.format( len(set_list) ))
    for brand in set_list:
        print(brand)

    return (call['selections']['years'] , set_list)
def get_selections_by_year(apiKey, year):
    call = requests.get('https://specifications.vinaudit.com/v3/selections?key=' + apiKey + '&list=year+make+model+trim&format=json').json()

    years_Arr = call['selections']['years']

    for x in years_Arr:
        yearName = x['name']
        if yearName == year:
            # specified year data
            SpecificMakes = x
            break

    SpecificMakes_arr = SpecificMakes['makes']


    for make in SpecificMakes_arr:
        print(make['name'])
        for model in make['models']:
            print(model['name'])
        print()
    
    return SpecificMakes_arr

# stats
def get_stats_VIN(apiKey , vinNumber):
    call = requests.get('https://specifications.vinaudit.com/v3/specifications?key='+ apiKey +'&format=json&include=attributes,equipment,colors,recalls,warranties,photos&vin='  +  vinNumber).json()


    for key , value in call['attributes'].items():
        print(f'{key}: \t {value}')

    print()

    for x in call['colors']:
        print('{} -- {}'.format(x['category'],x['name']))

    print()

    for x in call['equipments']:
        print('{} -- {}'.format(x['group'],x['name']))
    
    print()

    for x in call['recalls']:
        print('{} -- {}\n\nconsequence\n -- {}\n\nremedy\n -- {}'.format(x['components'],x['date'],x['consequence'],x['remedy']    ))
        print('----------------------------------------------------')
    
    print()



    return call
def get_stats_YMMT(apiKey , year , make , model , trim):
    call = requests.get('https://specifications.vinaudit.com/v3/specifications?format=json&key=' + apiKey + '&include=attributes,colors,equipment,recalls,warranties,photos&year='+ year + '&make='+make+'&model='+ model + '&trim='+trim).json()

    for key , value in call['attributes'].items():
        print(f'{key}: \t {value}')

    print()

    for x in call['colors']:
        print('{} -- {}'.format(x['category'],x['name']))

    print()

    for x in call['equipments']:
        print('{} -- {}'.format(x['group'],x['name']))
    
    print()

    for x in call['recalls']:
        print('{} -- {}\n\nconsequence\n -- {}\n\nremedy\n -- {}'.format(x['components'],x['date'],x['consequence'],x['remedy']    ))
        print('----------------------------------------------------')
    
    print()
    return call

# market data
def get_market_data_VIN(apiKey , vinNumber):
    call = requests.get('http://marketvalue.vinaudit.com/getmarketvalue.php?key='+ apiKey +'&format=json&period=90&mileage=average&vin='+ vinNumber).json()

    for key , value in call.items():
        print(key)
        pprint.pprint(value)
        print()
    
    return call
def get_market_data_PMYMMT(apiKey , period , mileage , year , make , model , trim):
    call = requests.get('http://marketvalue.vinaudit.com/getmarketvalue.php?key=' + apiKey + '&format=json&period='+ period +'&mileage='+ mileage +'&year='+ year +'&make='+ make +'&model='+ model +'&trim='+trim).json()

    for key , value in call.items():
        print(key)
        pprint.pprint(value)
        print()
    
    return call

# ownership costs
def get_ownershipCosts_VIN(apiKey , vinNumber):
    call = requests.get('http://ownershipcost.vinaudit.com/getownershipcost.php?key=JN4OLEOQXG4LPI0&state=WA&vin='+vinNumber).json()


    for key , value in call.items():
        # prints arrays for year 1,2,3,4,5
        print(key)
        pprint.pprint(value)
        print()

    # calculate costs without depretiation
    noDEPR_arr = [] 
    for x in range(5):
        noDEPR_arr.append(    call['total_cost'][x]  -  call['depreciation_cost'][x]     ) 
    call['total_cost_without_depreciation'] = noDEPR_arr
    print(f"Total Cost Without Depreciation\n{call['total_cost_without_depreciation']}")
    print()

    return call

# history report (create username and password!)
def get_HistoryVIN(apiKey , vinNumber , username, password):
    call = requests.get('https://api.vinaudit.com/v2/pullreport?id=00000000000002&key='+apiKey+'&vin='+ vinNumber + '&mode=test&user='+ username + '&pass='+password+'&format=json').json()

    pdfCall = requests.get('https://api.vinaudit.com/v2/pullreport?id=00000000000002&key='+apiKey+'&vin='+ vinNumber + '&mode=test&user='+ username + '&pass='+password+'&format=pdf')

    for key , value in call.items():
        print(key)
        pprint.pprint(value)
        print()
def get_HistoryVIN_RAWDATA(apiKey , vinNumber , username, password):
    call = requests.get('https://api.vinaudit.com/v2/report?id=94132583912&format=json').json()

    for key , value in call.items():
        print(key)
        pprint.pprint(value)
        print()

#car comparison
def car_comparisonVIN(apiKey , vinNumberONE , vinNumberTWO):

    # ATTRIBUTE COMPARISON
    car1 = get_stats_VIN(apiKey , vinNumberONE )
    car2 = get_stats_VIN(apiKey , vinNumberTWO)

    NumberOf_FeaturesComparison = {
        'attributes' :  (  len(car1['attributes'])  , len(car2['attributes'])  ),
        'equipments' :  (  len(car1['equipments'])  , len(car2['equipments'])  ),
        'warranties' :  (  len(car1['warranties'])  , len(car2['warranties'])  ),
        'colors' :  (  len(car1['colors'])  , len(car2['colors'])  ),
        'recalls' :  (  len(car1['recalls'])  , len(car2['recalls'])  ),
    }


    # MARKET DATA COMPARISON
    car1 = get_market_data_VIN(apiKey , vinNumberONE)
    car2 = get_market_data_VIN(apiKey , vinNumberTWO)

    marketDataComparison_Dictionary = {
        'vin' : ( car1['vin'] , car2['vin'] ),
        'vehicle' : ( car1['vehicle'] , car2['vehicle'] ),
        'mileage' : ( car1['mileage'] , car2['mileage'] ),
        'Sales_Analyzed' : ( car1['count'] , car2['count'] ),
        'mean' : ( car1['mean'] , car2['mean'] ),
        'Standard_Deviation' : ( car1['stdev'] , car2['stdev'] ),
        'Price_Certainty' : ( car1['certainty'] , car2['certainty'] ),
        'Period_of_Results' : ( car1['period'] , car2['period'] ),
        'prices' : ( car1['prices'] , car2['prices'] ),

    }


    #OWNERSHIP COST COMPARISON
    car1 = get_ownershipCosts_VIN(apiKey , vinNumberONE)
    car2 = get_ownershipCosts_VIN(apiKey , vinNumberTWO)
    
    ownershipCost_dictionary = {
        'vin' : ( car1['vin'] , car2['vin'] ),
        'mileage_start' : ( car1['mileage_start'] , car2['mileage_start'] ),
        'mileage_year' : ( car1['mileage_year'] , car2['mileage_year'] ),
        'vehicle' : ( car1['vehicle'] , car2['vehicle'] ),
        'depreciation_cost' : ( car1['depreciation_cost'] , car2['depreciation_cost'] ),
        'insurance_cost' : ( car1['insurance_cost'] , car2['insurance_cost'] ),
        'fuel_cost' : ( car1['fuel_cost'] , car2['fuel_cost'] ),
        'maintenance_cost' : ( car1['maintenance_cost'] , car2['maintenance_cost'] ),
        'repairs_cost' : ( car1['repairs_cost'] , car2['repairs_cost'] ),
        'fees_cost' : ( car1['fees_cost'] , car2['fees_cost'] ),
        'total_cost' : ( car1['total_cost'] , car2['total_cost'] ),
        'total_cost_sum' : ( car1['total_cost_sum'] , car2['total_cost_sum'] ),
        'total_cost_without_depreciation' : ( car1['total_cost_without_depreciation'] , car2['total_cost_without_depreciation'] ),
        
    }



    # CONSOLIDATE ALL DICTIONARIES INTO ONE
    consolidate = {
        'NumberOf_FeaturesComparison' : NumberOf_FeaturesComparison , 
        'marketDataComparison_Dictionary' : marketDataComparison_Dictionary , 
        'ownershipCost_dictionary' : ownershipCost_dictionary , 
    }






    # OUTPUT
    print('\n\n\nCOMPARISON RESULTS   < {} , {} >'.format( marketDataComparison_Dictionary["vehicle"][0] , marketDataComparison_Dictionary["vehicle"][1]))
    print('\n Number of features each car has:')
    pprint.pprint(NumberOf_FeaturesComparison)
    print('\n Market Data')
    pprint.pprint(marketDataComparison_Dictionary)
    print('\nOwnership Costs')
    pprint.pprint(ownershipCost_dictionary)
    
    # pprint.pprint(consolidate)

    return consolidate

# Car Outlook
def CompleteOutlookVIN(apiKey , vinNumberONE ):

    # ATTRIBUTE COMPARISON
    car1 = get_stats_VIN(apiKey , vinNumberONE )

    NumberOf_FeaturesComparison = {
        'attributes' :   len(car1['attributes'] ),
        'equipments' :   len(car1['equipments'] ),
        'warranties' :   len(car1['warranties'] ),
        'colors' : len(car1['colors'] ),
        'recalls' : len(car1['recalls']  ),
    }


    # MARKET DATA COMPARISON
    car1 = get_market_data_VIN(apiKey , vinNumberONE)

    marketDataComparison_Dictionary = {
        'vin' :  car1['vin'] ,
        'vehicle' :  car1['vehicle'] ,
        'mileage' :  car1['mileage'] ,
        'Sales_Analyzed' :  car1['count'],
        'mean' :  car1['mean'] ,
        'Standard_Deviation' :  car1['stdev'] ,
        'Price_Certainty' :  car1['certainty'],
        'Period_of_Results' :  car1['period'] ,
        'prices' :  car1['prices'],

    }


    #OWNERSHIP COST COMPARISON
    car1 = get_ownershipCosts_VIN(apiKey , vinNumberONE)
    
    ownershipCost_dictionary = {
        'vin' :  car1['vin'] ,
        'mileage_start' :  car1['mileage_start'] ,
        'mileage_year' :  car1['mileage_year'],
        'vehicle' :  car1['vehicle'] ,
        'depreciation_cost' :  car1['depreciation_cost'] ,
        'insurance_cost' : car1['insurance_cost'] ,
        'fuel_cost' : car1['fuel_cost'] ,
        'maintenance_cost' :  car1['maintenance_cost'] ,
        'repairs_cost' :  car1['repairs_cost'] ,
        'fees_cost' :  car1['fees_cost'] ,
        'total_cost' :  car1['total_cost'],
        'total_cost_sum' :  car1['total_cost_sum'],
        'total_cost_without_depreciation' : car1['total_cost_without_depreciation'] ,
        
    }



    # CONSOLIDATE ALL DICTIONARIES INTO ONE
    consolidate = {
        'NumberOf_FeaturesComparison' : NumberOf_FeaturesComparison , 
        'marketDataComparison_Dictionary' : marketDataComparison_Dictionary , 
        'ownershipCost_dictionary' : ownershipCost_dictionary , 
    }

    return consolidate




    # OUTPUT
    print('\n\n\nCOMPARISON RESULTS   <{}>'.format( marketDataComparison_Dictionary["vehicle"]) )
    print('\n Number of features the car has:')
    pprint.pprint(NumberOf_FeaturesComparison)
    print('\n Market Data')
    pprint.pprint(marketDataComparison_Dictionary)
    print('\nOwnership Costs')
    pprint.pprint(ownershipCost_dictionary)
    
    # pprint.pprint(consolidate)

    return consolidate


def main():
    print('Welcome to the car history app!')

    print('\n1 - Get Available Selections')
    print('2 - Get Available Selections by year')

    print('\n3 - Car Attributes VIN')
    print('4 - Car Attributes YMMT')

    print('\n5 - Market Data VIN')
    print('6 - Market Data YMMT')

    print('\n7 - Ownership Costs')

    print('\n8 - History Report')

    print('\n9 - Car Comparison')

    print('\n10 - Car COMPLETE OUTLOOK \n')

    option = input('Please choose an option!? : ')

    if option == '1':
        vinNumber = input("Please enter a Vin Number that you wanna look up!: ")
        get_available_selections( apiKey , vinNumber)
    
    elif option == '2':
        userInput = int(input('Please enter a year: '))
        get_selections_by_year(apiKey , userInput)
    
    elif option == '3':
        vinNumber = input("Please enter a Vin Number that you wanna look up!: ")
        get_stats_VIN(apiKey , vinNumber)
    
    elif option == '4':
        make = input('Please enter car brand: ')
        year = input('Please enter a year: ')
        model = input('Please enter the model: ')
        trim = input('Please enter trim type: ')
        get_stats_YMMT(apiKey , year , make , model ,trim )
    
    elif option == '5':
        vinNumber = input("Please enter a Vin Number that you wanna look up!: ")
        get_market_data_VIN(apiKey , vinNumber)
    
    elif option == '6':
        make = input('Please enter car brand: ')
        year = input('Please enter a year: ')
        model = input('Please enter the model: ')
        trim = input('Please enter trim type: ')
        get_market_data_PMYMMT(apiKey , '365' , 'average' , year , make , model , trim)
    
    elif option == '7':
        vinNumber = input("Please enter a Vin Number that you wanna look up!: ")
        get_ownershipCosts_VIN(apiKey , vinNumber)
    
    elif option == '8':
        vinNumber = input("Please enter a Vin Number that you wanna look up!: ")
        get_HistoryVIN(apiKey , vinNumber , 'username', 'password')
    
    elif option == '9':
        vinNumberONE = input("Please enter a Vin Number that you wanna look up!: ")
        vinNumberTWO = input("Please enter a Vin Number that you wanna look up!: ")
        car_comparisonVIN(apiKey , vinNumberONE , vinNumberTWO)

    elif option == '10':
        vinNumber = input("Please enter a Vin Number that you wanna look up!: ")
        CompleteOutlookVIN(apiKey , vinNumberONE )

    else:
        print('Please choose a valid response...')
        main()

main()