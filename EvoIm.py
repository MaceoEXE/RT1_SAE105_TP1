#ce projet aura pour objectif de montrer l'évolution
#de la population de l'agglomération immédiate
#et totale d'Auxerre

#cette partie est dédié à l'agglomération immédiate

import matplotlib.pyplot as plt
import csv

#table = []
#with open(fichier ,newline='') as csvfile:
#    reader=csv.reader(csvfile,delimiter=";")
#    for row in reader:
#        table.append(row)

ImLcommune =["Auxerre","Monéteau","Perrigny","Saint-Georges-sur-Baulche"]
ImNcommune = []
ImD2008 = []
ImD2016 = []
ImD2021 = []
ImD2023 = []

with open("metadonnees_communes.csv", encoding="utf-8",newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        if row[0] == "COM":
            if row [3] in ImLcommune and int(row[2])> 89000:
                ImNcommune.append(row[2])


with open("donnees_2008.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        if (row[2]+row[5]) in ImNcommune:
            ImD2008.append(row)

with open("donnees_2016.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        if (row[2]+row[5]) in ImNcommune:
            ImD2016.append(row)

with open("donnees_2021.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        if row [2] in ImNcommune:
            ImD2021.append(row)

with open("donnees_2023.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        if row [6] in ImNcommune:
            ImD2023.append(row)

#print(ImNcommune)
#print(ImD2008)
#print(ImD2016)
#print(ImD2021)
#print(ImD2023)

ImTot2008 = 0
for i in range(len(ImD2008)) :
    ImTot2008 += int(ImD2008[i-1][9])

ImTot2016 = 0
for i in range(len(ImD2016)):
    ImTot2016 += int(ImD2016[i-1][9])

ImTot2021 = 0 
for i in range(len(ImD2021)):
    ImTot2021 += int(ImD2021[i-1][5])

ImTot2023 = 0
for i in range(len(ImD2023)) :
    ImTot2023 += int(ImD2023[i-1][10])

#print(ImTot2008)
#print(ImTot2016)
#print(ImTot2021)
#print(ImTot2023)

def graphIm():
    plt.figure(figsize = (8, 8))
    x = [2008,2016,2021,2023]
    y = [ImTot2008, ImTot2016, ImTot2021, ImTot2023]
    plt.plot(x,y,"o-")
    plt.title("Population imédiate de l'aglomération d'Auxerre en fonction du temps")
    plt.xlabel("années")
    plt.ylabel("Nombre d'Habitants")
    plt.show() 