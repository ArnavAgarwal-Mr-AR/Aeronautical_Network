import networkx as nx
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
data_set=pd.read_csv("E:/SEM 5/Computer networks/Project/NA_11_Jun_29_2018_UTC11.CSV")
new_row = {'Flight No': "LHR", 'TimeStamp': 1530270000, 'Altitude': 0.0286, 'Longitude': -0.4543, 'Latitude': 51.4700}
new_df = pd.DataFrame([new_row])
data_set = pd.concat([data_set,new_df], ignore_index=True)
new_row = {'Flight No': "EWR", 'TimeStamp': 1530270000, 'Altitude': 0.003, 'Longitude': -74.1745, 'Latitude': 40.6895}
new_df = pd.DataFrame([new_row])
data_set = pd.concat([data_set,new_df], ignore_index=True)
length_of_dataset=len(data_set)
name = np.empty(length_of_dataset, dtype=object)
for i in range(length_of_dataset):
    name[i]=data_set.iloc[i][0]
def hvs(lng1, lt1, lng2, lt2):
    lng1, lt1, lng2, lt2 = map(math.radians, [lng1, lt1, lng2, lt2])
    dlon = lng2 - lng1 
    dlat = lt2 - lt1 
    temp = math.sin(dlat/2)**2 + math.cos(lt1) * math.cos(lt2) * math.sin(dlon/2)**2
    sqtemp = 2 * math.asin(math.sqrt(temp)) 
    radius = 6371 
    return sqtemp * radius
rows = length_of_dataset
cols = length_of_dataset
arr = np.zeros((rows, cols))
for i in range(length_of_dataset):
    for j in range (length_of_dataset
):
        
        lt1=data_set.iloc[i][3]
        lng1=data_set.iloc[i][4]
        lt2=data_set.iloc[j][3]
        lng2=data_set.iloc[j][4]
        arr[i][j]=hvs(lng1, lt1, lng2, lt2)
gra = nx.Graph()
for i in range (length_of_dataset):
    for j in range (length_of_dataset):
        gra.add_edge(name[i], name[j], weight=arr[i][j])

i=int(input("Enter node number"))
path1 = nx.single_source_dijkstra(gra, source='LHR', target=name[i])
path2 = nx.single_source_dijkstra(gra, source='EWR', target=name[i])
if(path1[0]<path2[0]):
    mylist=list(path1)
    if(mylist[0]>=500):
        mylist[0]=31.89
    elif(mylist[0]>=400):
        mylist[0]=43.505
    elif(mylist[0]>=300):
        mylist[0]=52.857
    elif(mylist[0]>=190):
        mylist[0]=63.970
    elif(mylist[0]>=90):
        mylist[0]=77.071
    elif(mylist[0]>=35):
        mylist[0]=93.854
    else:
        mylist[0]=119.130
    path1=tuple(mylist)
    print(path1)
        
else:
    mylist=list(path2)
    if(mylist[0]>=500):
        mylist[0]=31.89
    elif(mylist[0]>=400):
            mylist[0]=43.505
    elif(mylist[0]>=300):
            mylist[0]=52.857
    elif(mylist[0]>=190):
            mylist[0]=63.970
    elif(mylist[0]>=90):
            mylist[0]=77.071
    elif(mylist[0]>=35):
            mylist[0]=93.854
    else:
            mylist[0]=119.130
    path2=tuple(mylist)
    print(path2)