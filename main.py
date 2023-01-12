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
                list.append([microFrontend+"."+i, myDict[i]])


for i in data:
    print(i)
    printDict(data[i], i)

# with open("Arabic_Duplicates.csv", 'w', encoding='utf-8-sig', newline="") as csvfile:
#     csvWriter = csv.writer(csvfile)
#     for i in duplicates:
#         csvWriter.writerow(i)
#     print(duplicatesNum)
#     print(len(duplicates))

with open("Arabic_Unique.csv", 'w', encoding='utf-8-sig', newline="") as csvfile:
    csvWriter = csv.writer(csvfile)
    for i in list:
        csvWriter.writerow(i)

def checkDuplicateList(ele):
    for i in duplicates:
        if i[0] == ele:
            return True
    return False

uniqueValues = []
otherDuplicates = []

def checkOtherDuplicaes(ele):
    for i in otherDuplicates:
        if i[0] == ele:
            return True
    return False

def addOtherDuplicate(ele, key):
    for i in otherDuplicates:
        if i[0] == ele:
            i.append(key)
            return
    otherDuplicates.append([ele, key])

def removeDuplicates(myDict):
    global uniqueValues
    for i in myDict:
        if type(myDict[i]) == dict:
            return removeDuplicates(myDict[i])
        else:
            if checkDuplicateList(myDict[i]):
                # if not checkOtherDuplicaes(myDict[i]):
                #     uniqueValues.append([i, myDict[i]])
                addOtherDuplicate(myDict[i], i)
            else:
                uniqueValues.append([i, myDict[i]])
for i in data:
    uniqueValues = []
    otherDuplicates = []
    removeDuplicates(data[i])
    fileName = '%s_unique_en.csv' % i
    # with open(fileName, 'w', encoding='utf-8-sig', newline="") as csvfile:
    #     csvWriter = csv.writer(csvfile)
    #     for x in uniqueValues:
    #         csvWriter.writerow(x)
    # fileName = '%s_duplicates_en.csv' % i
    # with open(fileName, 'w', encoding='utf-8-sig', newline="") as csvfile:
    #     csvWriter = csv.writer(csvfile)
    #     for i in otherDuplicates:
    #         csvWriter.writerow(i)


f.close()