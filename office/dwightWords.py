#reading the csv file 
import csv
import re #reaplacing library
import nltk # for parts of speech recogn, this library should be downloaded
#nltk.download() #run only the first time

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

# put all the words spoken by micheal and their count in a dictionary 
wordsDict={}
noWordsDwight=0 #number of words micheal 

'''
condit=[Pos!='CONJ',
        Pos !='PRON',
        Pos !='PRT',
        Pos !='NN',
        Pos !='PRP',
        Pos !='VB']
'''

for row in allData:
    line=row[4] #line spoken
    tokens = nltk.word_tokenize(line)
    POSTagged = nltk.pos_tag(tokens)
    for word, Pos in POSTagged:
        wordFilt = word.lower()
        wordFilt = re.sub("[^a-zA-Z]+", "", wordFilt)
        if all([Pos!='CC',
                Pos!='TO',
                Pos!='DT',
                Pos!='IN',
                #Pos!='VBZ',
                Pos[0]!='V',
                Pos!='PRON',
                Pos!='PRT',
                Pos!='NN',
                Pos!='PRP',
                Pos!='PRP$',
                Pos!='EX',
                #Pos !='VB'
                ]):
            #everybodys words
            noWordsAll=noWordsAll +1
            if wordFilt in wordsDictAll:
                wordsDictAll[wordFilt] = wordsDictAll[wordFilt]+1
            else:
                wordsDictAll[wordFilt] = 1
            charName = row[5]#charecter name
            #only Dwight's words
            if 'dwight' in charName.lower():
                noWordsDwight=noWordsDwight+1
                if wordFilt in wordsDict:
                    wordsDict[wordFilt] = wordsDict[wordFilt]+1
                else:
                    wordsDict[wordFilt] = 1


# order by most popular word by everybody 
sorted_wordsDictAll= [(k, wordsDictAll[k]) for k in sorted(wordsDictAll, key=wordsDictAll.get, reverse = True)]


#looking at only the top 15 words by everybody 
wordsDictTopAll = sorted_wordsDictAll[:15]

with open('AllWords.csv', 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_wordsDictAll)
myfile.close()



# order by most popular word by micheal
sorted_wordsDict= [(k, wordsDict[k]) for k in sorted(wordsDict, key=wordsDict.get, reverse = True)]


#looking at only the top 15 words by micheal 
wordsDictTop = sorted_wordsDict[:15]

with open('DwightWords.csv', 'w') as myfile1:
     wr = csv.writer(myfile1, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_wordsDict)
myfile1.close()


#analysis

'''
(wordsSpokenByMicheal^2/wordsSpokenByEverybody) *(everyboysWordCount/MichealsWordCount)

'''
DwightWordFrac= noWordsAll/noWordsDwight


#loop for everyword spoken by micheal
uniqWordsDwight = {}

for k in wordsDict:
    if k in wordsDictAll:
        frac= ((wordsDict[k])**2/wordsDictAll[k])*DwightWordFrac
        uniqWordsDwight[k]= frac

        
    

# order by most popular word
sorted_uniqWordsDwight= [(k, uniqWordsDwight[k]) for k in sorted(uniqWordsDwight, key=uniqWordsDwight.get, reverse = True)]


#looking at only the top 15 words by micheal 
uniqWordsDwightTop = sorted_uniqWordsDwight[:15]

print(uniqWordsDwightTop)

with open('DwightWordsUnique.csv', 'w') as myfile2:
     wr = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_uniqWordsDwight)
myfile2.close()    


