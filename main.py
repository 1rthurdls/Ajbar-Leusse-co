import numpy as np
import matplotlib.pyplot as plt
import sys

temp_data = "data.txt"
columns_to_read1 = []
#task 1 
data_used = np.genfromtxt(temp_data, delimiter=',',dtype=None ,names=True,encoding=None,skip_header=1)

#task 2 
real_data=np.array(data_used,dtype=[('date', 'U10'), ('citi', 'U20'), ('col1', int), ('col2', int), ('col3', int), ('col4', int), ('col5', int), ('col6', int)] )

#task 3

def task3_1(real_data,city):
   
    locations = real_data['citi']
    cities = np.unique(locations)
    
    for citi in cities:
        if city in cities:
            city_data = real_data[locations == city]
        
            dates = city_data['date']
            max_temps = city_data['col1']
            min_temps = city_data['col2']
        
       
            avg_temps = (max_temps + min_temps) / 2
        else: 
            city_data = real_data[locations == citi]
        
            dates = city_data['date']
            max_temps = city_data['col1']
            min_temps = city_data['col2']
        
       
            avg_temps = (max_temps + min_temps) / 2

        
        plt.plot(dates, avg_temps, label=citi)
    

    plt.xlabel('Date')
    plt.ylabel('Average Temperature (C)')
    plt.title('Temperature Over Time for Each City')
    plt.legend()
    
    plt.show()


def task3_2(city):
    
    locations = real_data['citi']
    cities = np.unique(locations)

    if city not in cities :
        Max_temps = real_data[['citi','col1']]
        Min_temps = real_data[['citi','col2']]
    
    
        city_data = {}
        for citi, col1  in Max_temps:
            if citi not in city_data:
                city_data[citi] = []
            city_data[citi].append(col1)

        for citi, col2  in Min_temps:
            city_data[citi].append(col2)
    
        result = list(city_data.items())
   
        city_lists = {}

        for citi, col1 in result:
            city_lists[citi] = col1 
        
        for citi, col2 in result:
            city_lists[citi] = col2
    
        x = ['New York','Los Angeles','London','Tokyo','Beijing','Sydney','Paris','Berlin','Cairo','New Delhi']
        y= []
    
        for citi in x:
            haha = sum(city_lists[citi])/len(city_lists[citi])
            y.append(haha)

        plt.bar(x,y,label= "",width=1, edgecolor = 'black')
        plt.xticks( x, fontsize = 8)
        plt.title('average temperatures by city')
        plt.legend()
        plt.show()
"""      
task3_1(real_data,"Paris")
task3_2(real_data)
"""  

#task 5 
tempp_data = "Paris_data_climate.txt"
dataa_used = np.genfromtxt(tempp_data, delimiter=',',dtype=None ,names=True,encoding=None,skip_header=1)
reall_data=np.array(dataa_used,dtype=[('date', 'U10'), ('citi', 'U20'), ('col1', int), ('col2', int), ('col3', int), ('col4', int), ('col5', int), ('col6', int), ('col7', int), ('col8', int)] )

def aa():
    
    locations = reall_data['citi']
    cities = np.unique(locations)

    for city in cities:
        city_data = reall_data[locations == city]
        
       
        dates = city_data['date']

        max_temps = city_data['col1']
        min_temps = city_data['col2']
        avg_temps = (max_temps + min_temps) / 2

        pres = city_data['col3']
        co2 = city_data['col7']
        co2_used = co2 / 10
        sea = city_data['col8']

        plt.plot(dates, avg_temps, label="temp")
        plt.plot(dates, pres, label="pres")
        plt.plot(dates, co2_used, label="co2")
        plt.plot(dates, sea, label="sea")

    plt.xlabel('Date')
    plt.ylabel('Average Temperature (C)')
    plt.title('Temperature Over Time for Each City')
    plt.legend()
    
    plt.show()





