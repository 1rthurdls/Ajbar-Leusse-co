import sys
import Exercice2etexrecice4 as ex

if  len(sys.argv) < 2:
    print("this is a message for the user, in order for you toaccess the informaation you need, you need follow this structure")
    print("python 'name of the file' 'city your are interseted in' 'number of data you are searching'")
    print("we divided the data into mutiple categories that have a number ")
    print("if you are searching for the hottest and coldest day of a city, type 1")
    print("if you are searching for the overall hottest temperature's day of a city informations, type 2")
    print("if you are searching for the overall coldest temperature's day of a city informations, type 3")
    print("if you are searching for knowing if a day or a city was hot,moderate or cold, type 4")
    print("if you are searching for the average temperature of a city type 5")
    print("if you are searching for the total precipitation of a city type 6")
    print("if you are searching for maximum and minimum wind speed of a city type 7")
    sys.exit()

elif  len(sys.argv) ==3:

    city = str(sys.argv[1])
    number = int(sys.argv[2])

    if number == 7:
        listeville=["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney","Paris", "Berlin", "Cairo", "New Delhi"]
        
        if city in listeville:
            idx = ex.search(city,listeville)[0]
            print(ex.windspeedforeachcity()[idx])
    elif number == 6:
        listeville=["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney","Paris", "Berlin", "Cairo", "New Delhi"]
        
        if city in listeville:
            idx = ex.search(city,listeville)[0]
            print(ex.precipitation_for_each_city()[idx])
    
    elif number == 5:
        listeville=["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney","Paris", "Berlin", "Cairo", "New Delhi"]
        
        if city in listeville:
            idx = ex.search(city,listeville)[0]
            print(ex.averaget()[idx])

    elif number == 4:
        print(ex.avgteachday(city))
    
    elif number == 3:
        print(ex.overall_coldest_day(city))
    
    elif number == 2:
        print(ex.overall_hottest_day(city))
    
    elif number == 1:
         print(ex.hottestandcoldest(city))    

    else:
        sys.exit()