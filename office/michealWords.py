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

# put all the words spoken by everybody and their count in a dictionary 
wordsDictAll={} 
noWordsAll=0 #number of words all 

for row in allData:
    line=row[4] #line spoken
    for word in line.split():
        noWordsAll=noWordsAll +1
        wordFilt = word.lower()
        wordFilt = re.sub("[^a-zA-Z]+", "", wordFilt)
        if wordFilt in wordsDictAll:
            wordsDictAll[wordFilt] = wordsDictAll[wordFilt]+1
        else:
            wordsDictAll[wordFilt] = 1


# order by most popular word
sorted_wordsDictAll= [(k, wordsDictAll[k]) for k in sorted(wordsDictAll, key=wordsDictAll.get, reverse = True)]


#looking at only the top 15 words by micheal 
wordsDictTopAll = sorted_wordsDictAll[:15]

with open('AllWords.csv', 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_wordsDictAll)
myfile.close()


# put all the words spoken by micheal and their count in a dictionary 
wordsDict={}
noWordsMicheal=0 #number of words micheal 

for row in allData:
    charName = row[5]#charecter name
    if 'michael' in charName.lower():
        line=row[4] #line spoken
        #print(line)
        for word in line.split():
            noWordsMicheal=noWordsMicheal+1
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

with open('michealWords.csv', 'w') as myfile1:
     wr = csv.writer(myfile1, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_wordsDict)
myfile1.close()


#analysis

'''
(wordsSpokenByMicheal^2/wordsSpokenByEverybody) *(everyboysWordCount/MichealsWordCount)

'''
michealWordFrac= noWordsAll/noWordsMicheal


#loop for everyword spoken by micheal
uniqWordsMich = {}

for k in wordsDict:
    if k in wordsDictAll:
        frac= (wordsDict[k])**2/wordsDictAll[k]
        #print(frac)
        uniqWordsMich[k]= frac
        #*michealWordFrac
        #print(uniqWordsMich[k])
        
    

# order by most popular word
sorted_uniqWordsMich= [(k, uniqWordsMich[k]) for k in sorted(uniqWordsMich, key=uniqWordsMich.get, reverse = True)]


#looking at only the top 15 words by micheal 
uniqWordsMichTop = sorted_uniqWordsMich[:15]

with open('michealWordsUnique.csv', 'w') as myfile2:
     wr = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_uniqWordsMich)
myfile2.close()    


