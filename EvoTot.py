#ce projet aura pour objectif de montrer l'évolution
#de la population de l'agglomération immédiate
#et totale d'Auxerre

#cette partie est dédié à l'agglomération totale

import matplotlib.pyplot as plt
import csv

#table = []
#with open(fichier ,newline='') as csvfile:
#    reader=csv.reader(csvfile,delimiter=";")
#    for row in reader:
#        table.append(row)

TotLcommune = ["Appoigny","Augy","Auxerre","Bleigny-le-Carreau","Branches","Champs-sur-Yonne","Charbuy",
"Chevannes","Chitry","Coulanges-la-Vineuse","Escamps","Escolives Sainte-Camille","Gurgy",
"Gy-lEveque","Irancy","Jussy","Lindry, Moneteau","Montigny-la-Resle","Perrigny","Quenne",
"Saint-Bris-le-Vineux","Saint-Georges-sur-Baulche","Vallan","Venoy","Villefargeau","Villeneuve","Saint-Salves","Vincelles","Vincelottes"]
Ncommune = []
TotD2008 = []
TOtD2016 = []
TotD2021 = []
TotD2023 = []

with open("metadonnees_communes.csv", encoding="utf-8",newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        if row[0] == "COM":
            if row [3] in TotLcommune and int(row[2])> 89000:
                Ncommune.append(row[2])


with open("donnees_2008.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        if (row[2]+row[5]) in Ncommune:
            TotD2008.append(row)

with open("donnees_2016.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        if (row[2]+row[5]) in Ncommune:
            TOtD2016.append(row)

with open("donnees_2021.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        if row [2] in Ncommune:
            TotD2021.append(row)

with open("donnees_2023.csv", newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        if row [6] in Ncommune:
            TotD2023.append(row)

#print(Ncommune)
#print(TotD2008)
#print(TOtD2016)
#print(TotD2021)
#print(TotD2023)

Tot2008 = 0
for i in range(len(TotD2008)) :
    Tot2008 += int(TotD2008[i-1][9])

Tot2016 = 0
for i in range(len(TOtD2016)):
    Tot2016 += int(TOtD2016[i-1][9])

Tot2021 = 0 
for i in range(len(TotD2021)):
    Tot2021 += int(TotD2021[i-1][5])

Tot2023 = 0
for i in range(len(TotD2023)) :
    Tot2023 += int(TotD2023[i-1][10])

#print(Tot2008)
#print(Tot2016)
#print(Tot2021)
#print(Tot2023)

def graphTot():
    plt.figure(figsize = (8, 8))
    x = [2008,2016,2021,2023]
    y = [Tot2008, Tot2016, Tot2021, Tot2023]
    plt.plot(x,y,"ro-")
    plt.title("Population total de l'aglomération d'Auxerre en fonction du temps")
    plt.xlabel("années")
    plt.ylabel("Nombre d'Habitants")
    plt.show() 