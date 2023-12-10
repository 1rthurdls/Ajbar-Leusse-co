import numpy as np

# Load the data
data_path = "C:\\Users\\cestm\\Downloads\\Ajbar-Leusse-co-main\\data.txt"
data = np.loadtxt(data_path, delimiter=",", dtype=str, skiprows=1)
x= np.array(data)
#exercice 2a
def listoftmax():
    liste_of_tmax=[]
    for i in range(310):
        liste_of_tmax.append(int(x[i][2]))
    return liste_of_tmax

def listoftmin():
    liste_of_tmin=[]
    for i in range(310):
        liste_of_tmin.append(int(x[i][3]))
    return liste_of_tmin

def listofcities():
    liste_of_cities=[]
    for i in range(310):
        liste_of_cities.append(x[i][1])
    return liste_of_cities

def averaget():
    nameofcities = ["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney", "Paris", "Berlin", "Cairo", "New Delhi"]
    liste_of_cities = listofcities()
    result=[]
    tmax = listoftmax()
    tmin = listoftmin()
    i=0
    for city in nameofcities:
        tcity=[]
        while i < len(liste_of_cities) and liste_of_cities[i] == city:
            tcity.append(int(tmax[i]))
            tcity.append(int(tmin[i]))
            i+=1
        result.append((city,np.average(tcity)))
    return result
#_______________________________________________



#exercice 2b
def listeofprecipitations():
    liste_of_precipitations=[]
    for j in range(310):
        liste_of_precipitations.append(x[j][4])
    return liste_of_precipitations

def precipitation_for_each_city():
    nameofcities = ["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney", "Paris", "Berlin", "Cairo", "New Delhi"]
    liste_of_cities = listofcities()
    liste_of_precipitations = listeofprecipitations()
    result = []
    i=0
    for city in nameofcities:
        totalprecip = 0
        while i < len(liste_of_cities) and liste_of_cities[i] == city:
            totalprecip += float(liste_of_precipitations[i])
            i += 1
        result.append((city, totalprecip))
    
    return result 
#________________________________________________________
#exercice 2c
def wind_speed():
    windspeed=[]
    for j in range(310):
        windspeed.append(x[j][5])
    return windspeed

def Humidity():
    humidity=[]
    for j in range(310):
        humidity.append(x[j][6])
    return humidity

def Cloud_Cover():
    cloud_cover=[]
    for j in range(310):
        cloud_cover.append(x[j][7])
    return cloud_cover

def windspeedforeachcity():
    nameofcities = ["New York", "Los Angeles", "London", "Tokyo", "Beijing", "Sydney", "Paris", "Berlin", "Cairo", "New Delhi"]
    liste_of_cities = listofcities()
    result=[]
    vitesseduvent = wind_speed()
    i=0
    for city in nameofcities:
        wind_speed_of_city=[]
        while i < len(liste_of_cities) and liste_of_cities[i] == city:
            wind_speed_of_city.append(int(vitesseduvent[i]))
            i+=1
        result.append((city,max(wind_speed_of_city),min(wind_speed_of_city)))
    return result
#_______________________________________________________

# exercice 4a 

def search(x, y):
    listidx = []
    i=0
    while i < len(y):
        if y[i]==x:
            listidx.append(i)
            i+=1
        else :
            i+=1
    return listidx


def avgteachday(city):
    tmax = listoftmax()
    tmin = listoftmin()
    cities = listofcities()
    idxx = search(city, cities)
    avgt = []
    for i in idxx:
        avg_temp = np.average([int(tmin[i]), int(tmax[i])])
        if 12 <= avg_temp <= 22:
            category = "moderate"
        elif avg_temp < 12:
            category = "cold"
        else:
            category = "hot"
        avgt.append((avg_temp, category))
    return [city, avgt]

#__________________________________________________________

#ecercice 4b

def averagetttt():
    average=[]
    for i in range(len(listoftmax())):
        average.append((listoftmax()[i] + listoftmin()[i]) / 2)
    return average




def listofdate():
    liste_of_date=[]
    for i in range(310):
        liste_of_date.append(x[i][0])
    return liste_of_date


def hottestandcoldest(city):
    dates = listofdate()
    cities = listofcities()
    tmax = listoftmax()
    tmin = listoftmin()
    listtmoyenne =[]

    avgt =averagetttt()

    idx_city = search(city, cities)
    
    for i in idx_city:

        listtmoyenne.append((tmax[i] + tmin[i]) / 2)

    tempmax=max(listtmoyenne)
    tempmin=min(listtmoyenne)
    
    idx_max = search(tempmax,avgt[idx_city[0]:idx_city[-1]+1])

    idx_min = search(tempmin,avgt[idx_city[0]:idx_city[-1]+1])
 
    idxx_max =idx_city[idx_max[0]]
    idxx_min = idx_city[idx_min[0]]

    return city, "hottest day :",dates[idxx_max],"Maximum Temperature :",listoftmax()[idxx_max],"Minumum Temperature",listoftmin()[idxx_max],"Precipitation :",listeofprecipitations()[idxx_max],"Wind Speed :",wind_speed()[idxx_max],"Humidity :",Humidity()[idxx_max],"Cloud Cover :",Cloud_Cover()[idxx_max],"coldest day :",dates[idxx_min],"Maximum Temperature :",listoftmax()[idxx_min],"Minumum Temperature",listoftmin()[idxx_min],"Precipitation :",listeofprecipitations()[idxx_min],"Wind Speed :",wind_speed()[idxx_min],"Humidity :",Humidity()[idxx_min],"Cloud Cover :",Cloud_Cover()[idxx_min]
    

#_________________________________________________________________________________
# Execcice 4c

print(hottestandcoldest("Los Angeles"))
print(hottestandcoldest("London"))
print(hottestandcoldest("Tokyo"))
print(hottestandcoldest("Beijing"))
print(hottestandcoldest("Sydney"))
print(hottestandcoldest("Berlin"))
print(hottestandcoldest("Cairo"))
print(hottestandcoldest("New Delhi"))


#________________________________________________________
#Exercice 4d
"""
On Los Angeles hottest day,its highest temperature is the higgest of January and its lowest Temperature is the second highest of January. 
The cloud cover is very low with only 8% wich is tghe second lowest of January and the Humidity is also very Low (the second lowest of January).
On its coldest day, The maximum temperature is the smallest of the month, and its coldest is the coldest of the month. The cloud cover is Kind of low
In comparison with the average of the month and the rest of are in the average of the month. 




"""


#___________________________________________________________
#Exercice 4e
def overall_hottest_day(city):
    dates = listofdate()
    cities = listofcities()
    tmax = listoftmax()
    
    idx_city = search(city, cities)

    list_t_city=tmax[int(idx_city[0]):int(idx_city[-1])+1]

    temperature_max_city = max(list_t_city)

    idxtmax = search(temperature_max_city,list_t_city)[0]

    date_temperature_maximale=dates[idxtmax]
    return "Date :",date_temperature_maximale,"Maximum Temperature :",temperature_max_city,"Minumum Temperature",listoftmin()[idxtmax],"Precipitation :",listeofprecipitations()[idxtmax],"Wind speed :",wind_speed()[idxtmax],"Humidity :",Humidity()[idxtmax],"Cloud Cover :",Cloud_Cover()[idxtmax]


#____________________________________________________
#Exercice 4f
def overall_coldest_day(city):
    tmin = listoftmin()

    dates = listofdate()

    cities=listofcities()

    tavgt=averagetttt()

    idxx=search(city,cities)

    list_t_city=tmin[int(idxx[0]):int(idxx[-1])+1]

    tempmin=min(list_t_city)

    mindidxdecity = search(tempmin,list_t_city)[0]

    date= dates[mindidxdecity]
    
    return "Date :",date,"Minumum Temperature :",tempmin,"Maximum Temperature",listoftmax()[mindidxdecity],"Precipitation :",listeofprecipitations()[mindidxdecity],"Wind speed :",wind_speed()[mindidxdecity],"Humidity :",Humidity()[mindidxdecity],"Cloud Cover :",Cloud_Cover()[mindidxdecity]

#_____________________________________________________________________________
#Excercice 6







