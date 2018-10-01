#Import de la bibliothèque "date"
from datetime import datetime

#Recupération de la date de l'utilisateur
result = input("Entrez le jour de la semaine à calculer sous le format JJMMAAAA : ")
dDate = datetime.strptime(result, '%d%m%Y')
iAA = int(dDate.strftime('%y'))
iDay = int(dDate.strftime('%d'))
iMonth = int(dDate.strftime('%m'))
isBissex = False

# 1) 2)
iCal = (iAA + (iAA / 4))

# 3)
iCal += iDay

# 4)
if 2 == iMonth:
    iCal += 3
elif iMonth == 3:
    iCal += 3
elif iMonth == 4:
    iCal += 6
elif iMonth == 5:
    iCal += 1
elif iMonth == 6:
    iCal += 4
elif iMonth == 7:
    iCal += 6
elif iMonth == 8:
    iCal += 2
elif iMonth == 9:
    iCal += 5
elif iMonth == 11:
    iCal += 3
elif iMonth == 12:
    iCal += 5

iYear = int(dDate.strftime('%Y'))

if iYear % 400 == 0:
    isBissex = True
elif iYear % 100 == 0:
    isBissex = False
elif iYear % 4 == 0:
    isBissex = True

if isBissex:
    if iMonth == 1 or iMonth == 2:
        iCal = iCal - 1

# 6)
tmp = iYear - iAA
if tmp == 1600:
    iCal += 6
elif tmp == 1700:
    iCal += 4
elif tmp == 1800:
    iCal += 2
elif tmp == 1900:
    iCal += 0
elif tmp == 2000:
    iCal += 6
elif tmp == 2100:
    iCal += 4

# 7)
iCal = iCal % 7

# Résultat

listJ = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

indx = len(listJ)
for i in range(len(listJ)):
    if i == int(iCal):
        print("C'est un : ", listJ[i])
        break
