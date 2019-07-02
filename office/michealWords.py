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
noWordsMicheal=0 #number of words micheal 



for row in allData:
    line=row[4] #line spoken
    tokens = nltk.word_tokenize(line)
    POSTagged = nltk.pos_tag(tokens)
    for word, Pos in POSTagged:
        wordFilt = word.lower()
        wordFilt = re.sub("[^a-zA-Z]+", "", wordFilt)
        if Pos != 'CONJ' or Pos !='PRON' or Pos !='PRT'or Pos !='NN'or Pos !='PRP':
            noWordsAll=noWordsAll +1
            if wordFilt in wordsDictAll:
                wordsDictAll[wordFilt] = wordsDictAll[wordFilt]+1
            else:
                wordsDictAll[wordFilt] = 1
            charName = row[5]#charecter name
            if 'michael' in charName.lower():
                noWordsMicheal=noWordsMicheal+1
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
        frac= (wordsDict[k])**2/wordsDictAll[k]*michealWordFrac
        uniqWordsMich[k]= frac

        
    

# order by most popular word
sorted_uniqWordsMich= [(k, uniqWordsMich[k]) for k in sorted(uniqWordsMich, key=uniqWordsMich.get, reverse = True)]


#looking at only the top 15 words by micheal 
uniqWordsMichTop = sorted_uniqWordsMich[:15]

print(uniqWordsMichTop)

with open('michealWordsUnique.csv', 'w') as myfile2:
     wr = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
     wr.writerows(sorted_uniqWordsMich)
myfile2.close()    


