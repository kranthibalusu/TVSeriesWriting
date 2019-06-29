#reading the csv file 
import csv
import re

#read and sparse data
f = open("the-office-lines.csv",'r')
csvreader = csv.reader(f)
allData = list(csvreader)
#delete first row, header
del allData[0]
f.close()

#total no of lines
lineNo = allData.__len__()
print(lineNo)

# put all the words spoken m y micheal and their count in a dictionary 
wordsDict={}

for row in allData:
    charName = row[5]#charecter name
    if 'phyllis' in charName.lower():
        line=row[4] #line spoken
        #print(line)
        for word in line.split():
            wordFilt = word.lower()
            wordFilt = re.sub("[^a-zA-Z]+", "", wordFilt)
            if wordFilt in wordsDict:
                wordsDict[wordFilt] = wordsDict[wordFilt]+1
            else:
                wordsDict[wordFilt] = 1


# order by most popular word
sorted_wordsDict= [(k, wordsDict[k]) for k in sorted(wordsDict, key=wordsDict.get, reverse = True)]


#looking at only the top 15 words by micheal 
wordsDictTop = sorted_wordsDict[:15]

with open('phyllisWords.csv', 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_wordsDict)
myfile.close()



