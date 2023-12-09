import numpy as np
data_path="C:\\Users\\cestm\\Downloads\\Ajbar-Leusse-co-main\\data.txt"
data = np.loadtxt(data_path,delimiter=",",dtype=str,skiprows=1)
x= np.array(data)
#Exercice 2a
def listoftmax():
    liste_of_tmax=[]
    for i in range(310):
        liste_of_tmax.append(x[i][2])
    return liste_of_tmax

def listoftmin():
    liste_of_tmin=[]
    for i in range(310):
        liste_of_tmin.append(x[i][3])
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
print(averaget())
#Exercice 2b
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
#Exercice 2c
def wind_speed():
    windspeed=[]
    for j in range(310):
        windspeed.append(x[j][5])
    return windspeed


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


