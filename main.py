import json
import csv

f = open('ar.json', 'r', encoding="utf-8")

data = json.load(f)

list = []

duplicates = []
duplicatesNum = 0

def checkDuplicate(ele):
    for i in list:
        if i[1] == ele:
            return True
    return False

def addDuplicate(ele, header, microFrontend):
    global duplicatesNum
    global duplicates
    for i in duplicates:
        if i[0] == ele:
            i.append(microFrontend+"."+header)
            return
    header1 = ""
    for i in list:
        if i[1] == ele:
            header1 = i[0]
    duplicates.append([ele, microFrontend+"."+header1, microFrontend+"."+header])
    duplicatesNum += 1


def printDict(myDict, microFrontend):
    global list
    for i in myDict:
        if type(myDict[i]) == dict:
            return printDict(myDict[i], microFrontend)
        else:
            if checkDuplicate(myDict[i]):
                addDuplicate(myDict[i], i, microFrontend)
            else:
                list.append([i, myDict[i]])


for i in data:
    print(i)
    printDict(data[i], i)

with open("output_Duplicates.csv", 'w', encoding='utf-8-sig', newline="") as csvfile:
    csvWriter = csv.writer(csvfile)
    for i in duplicates:
        csvWriter.writerow(i)
    print(duplicatesNum)
    print(len(duplicates))
    



f.close()