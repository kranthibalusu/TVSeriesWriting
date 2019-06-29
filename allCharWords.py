#reading the csv file 
import csv
import operator

#read and sparse data
f = open("the-office-lines.csv",'r')
csvreader = csv.reader(f)
allData = list(csvreader)
#delete first row, header
del allData[0]

#total no of lines
lineNo = allData.__len__()
print(lineNo)

#find all charecters
charDict={}
vineel
for row in allData:
    charName = row[5]#charecter name 
    if charName in charDict:
        charDict[charName] = charDict[charName]+1
    else:
        charDict[charName] = 0

#print all the dictionary data 
#print(charDict)


# order by number or lines 
sorted_charDict= [(k, charDict[k]) for k in sorted(charDict, key=charDict.get, reverse = True)]

#print(sorted_charDict)

#looking at only the top 15 speaking charecters 
charDictTop = sorted_charDict[:15]
#print(charDictTop)


with open('topLines.csv', 'w+') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(charDictTop)

