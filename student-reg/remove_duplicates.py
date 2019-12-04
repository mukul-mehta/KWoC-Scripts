import csv
import os

emailMap = {}
nameMap = {}
rowList = []

with open("new_data.csv") as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for row in reader:
        name = row[0]
        handle = row[1]
        email = row[2]
        college = row[3]
        row = [name, handle, email, college]
        rowList.append(row)

        if email not in emailMap:
            emailMap[email] = 1
        else:
            emailMap[email] += 1
        
        if name not in nameMap:
            nameMap[name] = 1
        else:
            nameMap[name] += 1

with open("new_data2.csv", "w+") as newFile:
    writer = csv.writer(newFile)
    for row in rowList:
        if nameMap[row[0]] == 1 and emailMap[row[2]] == 1:
            writer.writerow(row)

        elif nameMap[row[0]] != 1:
            nameRepeats = [i for i, x in enumerate(rowList) if x[0] == row[0]]
            for name in nameRepeats:
                print(str(name) + " - " + str(rowList[name]))
            try:
                x = input("Which elements to keep: ")
                x = x.split()
                for i in x:
                    i = int(i)
                    writer.writerow(rowList[i])
            except:
                for name in nameRepeats:
                    writer.writerow(rowList[name])
        
        elif emailMap[row[2]] != 1:
            nameRepeats = [i for i, x in enumerate(rowList) if x[2] == row[2]]
            for name in nameRepeats:
                print(str(name) + " - " + str(rowList[name]))
            try:
                x = input("Which elements to keep: ")
                x = x.split()
                for i in x:
                    i = int(i)
                    writer.writerow(rowList[i])
            except:
                for name in nameRepeats:
                    writer.writerow(rowList[name])

