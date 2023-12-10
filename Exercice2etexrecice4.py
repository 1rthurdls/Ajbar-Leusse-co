import numpy as np
import sys



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

def listofdate():
    liste_of_date=[]
    for i in range(310):
        liste_of_date.append(x[i][0])
    return liste_of_date

def avgteachday(city):
    tmax = listoftmax()
    tmin = listoftmin()
    cities = listofcities()
    idxx = search(city, cities)
    avgt = []
    list_of_date = listofdate()
    date = list_of_date[int(idxx[0]):int(idxx[-1])+1]
    
    for i in idxx:
        avg_temp = ((tmax[i] + tmin[i]) / 2)
        if 12 <= avg_temp <= 22:
            category = "moderate"
        elif avg_temp < 12:
            category = "cold"
        else:
            category = "hot"
        avgt.append((list_of_date[i],avg_temp, category))
    
    return [city, avgt]

#__________________________________________________________

#ecercice 4b

def averagetttt():
    average=[]
    for i in range(len(listoftmax())):
        average.append((listoftmax()[i] + listoftmin()[i]) / 2)
    return average



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


In New York, the combination of high humidity (65-85%), variable wind speed (10-25 km/h), frequent precipitation, and moderate cloud cover suggests are the cause of such low temperatures.

Los Angeles, with its lower humidity (48-90%), moderate winds (12-20 km/h), absence of precipitation, and low to moderate cloud cover, reflects way hotter temperature and very variable ones(from 25-10 °c). 

London's high humidity (68-90%), moderate to high winds (12-25 km/h), regular precipitation, and high cloud cover indicate such low temperature and such a low variation of temperature.

Tokyo's moderate humidity (55-90%), winds (10-22 km/h), low precipitation, and variable cloud cover suggest a 
moderate and cold temperature with still a big variation(16-0 °c)

Beijing, with lower humidity (36-50%), varying winds (10-22 km/h), very low precipitation, and low cloud cover, are the cause of cold temperature

Let's not forget that these two lasts country have temperature that variate aa lot because of the monsoon Which is a process that makes the temperature variation between winter and summer not to extreme.


Sydney's moderate humidity (35-45%), winds (14-20 km/h), very low precipitation, and low cloud cover are characteristic of warm and not variable temperatures.

Paris and Berlin, both with high humidity (68-92%), moderate winds (14-24 km/h), some precipitation, and moderate to high cloud cover, exhibit a very temperete climate with very low variations of temperature and temperatures that are moderate.

 Cairo's very low humidity (35-42%), moderate winds (14-20 km/h), absence of precipitation, and variable cloud cover typify an arid desert climate with mostly high temperature that range from(29-8)

 Finally,New Delhi's moderate to high humidity (48-65%), winds (10-22 km/h), minimal precipitation, and low cloud cover suggest hot temperatures with a big difference between the highest temperature ofthe day and the lower ones.

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






