import sys
import Exercice2etexrecice4 as ex
import main as mn
import numpy as np

#global variable
listeville=["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney","Paris", "Berlin", "Cairo", "New Delhi","All"]


temp_data = "C:\\Users\\cestm\\Downloads\\Ajbar-Leusse-co-main\\data.txt"
columns_to_read1 = []

data_used = np.genfromtxt(temp_data, delimiter=',',dtype=None ,names=True,encoding=None,skip_header=1)

real_data=np.array(data_used,dtype=[('date', 'U10'), ('citi', 'U20'), ('col1', int), ('col2', int), ('col3', int), ('col4', int), ('col5', int), ('col6', int)] )

tempp_data = "C:\\Users\\cestm\\Downloads\\Ajbar-Leusse-co-main\\Paris_data_climate.txt"
dataa_used = np.genfromtxt(tempp_data, delimiter=',',dtype=None ,names=True,encoding=None,skip_header=1)
reall_data=np.array(dataa_used,dtype=[('date', 'U10'), ('citi', 'U20'), ('col1', int), ('col2', int), ('col3', int), ('col4', int), ('col5', int), ('col6', int), ('col7', int), ('col8', int)] )










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
    print("if you are searching for a graph representing the temperature over time of a city type 8")
    print("if you are searching for a bar chart that compares the average temperature of the different cities type All as if it was a city then type 9.")
    print("if you are searching for a chart that illustrate the relationship between temperature, precipitation, and climate change factors type All as if it was a city then type 10.")

    sys.exit()

elif  len(sys.argv) ==3:

    city = str(sys.argv[1])
    number = str(sys.argv[2])

    if number == '7':
        
        if city in listeville:
            idx = ex.search(city,listeville)[0]
            print(ex.windspeedforeachcity()[idx])
            sys.exit()
        else:
            print("ERROR,errortype city not in database")
            sys.exit()
    elif number == '6':
        
        if city in listeville:
            idx = ex.search(city,listeville)[0]
            print(ex.precipitation_for_each_city()[idx])
            sys.exit()
        else:
            print("ERROR,errortype city not in database")
            sys.exit()

    elif number == '5':
        
        if city in listeville:
            idx = ex.search(city,listeville)[0]
            print(ex.averaget()[idx])
            sys.exit()
        else:
            print("ERROR,errortype city not in database")
            sys.exit()

    elif number == '4':
        if city in listeville:
            print(ex.avgteachday(city))
            sys.exit()
        else :
            print("ERROR,errortype city not in database")
            sys.exit()

    elif number == '3':
        if city in listeville:
            print(ex.overall_coldest_day(city))
            sys.exit()
        else :
            print("ERROR,errortype city not in database")
            sys.exit()
    
    elif number == '2':
        if city in listeville:
            print(ex.overall_hottest_day(city))
            sys.exit()
        else :
            print("ERROR,errortype city not in database")
            sys.exit()
    
    elif number == '1':
        if city in listeville:
            print(ex.hottestandcoldest(city))
            sys.exit()   
        else :
             print("ERROR,errortype city not in database")
             sys.exit()
    elif number == '8':
        if city in listeville:
            print(mn.task3_1(real_data,city))
            sys.exit()   
        else :
             print("ERROR,errortype city not in database")
             sys.exit()

    elif number ==  '9':
        if city in listeville:
            print(mn.task3_2(city))
            sys.exit()   
        else :
             print("ERROR,errortype city not in database")
             sys.exit()
    
    elif number == '10':
        if city in listeville:
            print(mn.aa())
            sys.exit() 
        else :
             print("ERROR,errortype city not in database")
             sys.exit()
    
    else :
            print("ERROR,errortype city not in database")
            sys.exit()


    

            
elif  len(sys.argv) >3:
    print("ERROR, errortype: too many arguments were given")
    sys.exit()


    
        
    



    
