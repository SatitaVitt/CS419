import sys
from array import *
import time

startTime = time.time()

listOfLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']

def listPossible2():
    #aa = 27
    #possibleList = [[0 for x in range(aa)] for y in range(aa)]
    possibleList = []
    i = 0
    j = 0
    count2 = 0
    while i < 27:
        while j < 27:
            possibleList.append(00)  
            possibleList[count2] = listOfLetters[i]+listOfLetters[j]
            count2 += 1
            j += 1
        i += 1
        j = 0
    #print("count2 = ", count2)
    return possibleList

def listPossible3(listPossibleOf2):
    i = 0
    j = 0
    count3 = 0
    possibleList3 = []
    while i < len(listPossibleOf2):
        while j < 27:
            possibleList3.append(000)  
            possibleList3[count3] = listPossibleOf2[i]+listOfLetters[j]
            count3 += 1
            j += 1
        i += 1
        j = 0
    #print(possibleList3)
    #print("count3 = ", count3)
    return possibleList3

def listPossibleN(N, listPossibleOf2, listPossibleOf3):
    if N == 2:
	return listPossibleOf2
    elif N == 3:
	return listPossibleOf3
    elif N == 1:
	return listOfLetters

    possibleListN = []
    if N % 2 == 0:
    	#this is an even number of N
    	numTimeBi = N/2
    	i = 0
    	j = 0
	k = 1
    	countN = 0
    	possibleListNtemp = listPossibleOf2
	while k < numTimeBi:
    	    while i < len(possibleListNtemp):
	        while j <len(listPossibleOf2):
		    possibleListN.append(0)
		    possibleListN[countN] = possibleListNtemp[i]+listPossibleOf2[j]
		    countN += 1
		    j += 1
		i += 1
		j = 0
	    #print(possibleListN)
	    
	    del possibleListNtemp[:]
	    #print(possibleListNtemp)
	    #possibleListNtemp = []
	    #print("--------------------------")
	    possibleListNtemp = possibleListN
	    return possibleListNtemp
	    #print(possibleListNtemp)
	    #del possibleListN[:]
	    
	    possibleListN = []
	    countN = 0
	    i = 0
	    k += 1
	#return possibleListNtemp
    else:
        #this is an even number of N
    	numTimeBi = (N-3)/2
    	i = 0
    	j = 0
	k = 1
    	countN = 0
    	possibleListNtemp = listPossibleOf2
	while k < numTimeBi:
    	    while i < len(possibleListNtemp):
	        while j <len(listPossibleOf2):
		    possibleListN.append(0)
		    possibleListN[countN] = possibleListNtemp[i]+listPossibleOf2[j]
		    countN += 1
		    j += 1
		i += 1
		j = 0
	    del possibleListNtemp[:]
	    possibleListNtemp = possibleListN
	    del possibleListN[:]
	    countN = 0
	    i = 0
	    k += 1
	if i != 0:
	    print("REPORT!!!!!! ERROR!!!!!\n\n\n\n\n\n")
	while i < len(possibleListNtemp):
	    while j < len(ListPossibleOf3):
		possibleListN.append(0)
		possibleListN[countN] = possibleListNtemp[i]+listPossibleOf3[j]
		countN +=1
		j += 1
	    i += 1
	    j = 0
	return possibleListN
    return possibleListNtemp


def freqAnalysis(FileName, possibleList, length):
    j = 0
    g = 0
    space = ' '
    aa = len(possibleList)
    while g < length:
	space = space + space
	g += 1
    #print(aa)
    countingList = [0 for x in range(aa)]
    file = open(FileName, "r")
    for line in file:
        #print line
        i = 0
        while i < len(line)-1:
	    s = i
	    #print("i: ", line[s])
	    while s < s+length:
		if line[s] in listOfLetters:
		    #DO NOTHING
		    s = s 
		else:
		    i = s+1
		    break
		s += 1
            gram2 = ''.join(line[i:i+length])
	    if gram2 == space:
		i = i + 1
		continue
	    gram2 = gram2.lower()
            #print(gram2)
            while j < len(possibleList):
                if gram2 == possibleList[j]:
		    #if length == 3:
			#print(gram2)
                    countingList[j] += 1
                    break
                j += 1
            i += 1
            j = 0
    file.close()
    
    adjustedPossibleList = []
    adjustedCountingList = []
    i = 0
    j = 0
    h = 0

    while i < len(countingList):
	if countingList[i] > h:
	    adjustedPossibleList.append(0)
	    adjustedCountingList.append(0)
	    #print(adjustedPossibleList)
	    adjustedPossibleList[j] = possibleList[i]
	    adjustedCountingList[j] = countingList[i]
	    j += 1
	i += 1

    return adjustedCountingList, adjustedPossibleList


def sortingLists(SortingListNum1, SortingListLetter1, SortingListNum2, SortingListLetter2, Num):
  #SortingList1 = cipher text, sortinglist2 = known text
  
    Cipher = sorted(SortingListNum1, reverse = True)
    Known = sorted(SortingListNum2, reverse = True)
    ww = len(SortingListNum1)
    ww2 = len(SortingListNum2)
    if ww > ww2:
	ww = ww2

    mappingList = [['?' for x in range(ww)] for y in range(2)]
    
    j = 0
    i = 0

    SortingLetter1 = SortingListLetter1
    SortingLetter2 = SortingListLetter2
    SortingNum1 = SortingListNum1
    SortingNum2 = SortingListNum2


    while i < len(Cipher):
	if i < len(Cipher)-1:
	    if Cipher[i] == Cipher[i+1]:
		#SortingListLetter1.pop(SortingListNum1.index(Cipher[i]))
		mappingList[0][j] = SortingLetter1[SortingNum1.index(Cipher[i])]
		del SortingLetter1[SortingNum1.index(Cipher[i])]
		del SortingNum1[SortingNum1.index(Cipher[i])]

	    else:
		mappingList[0][j] = SortingLetter1[SortingNum1.index(Cipher[i])]
	    if Known[i] == Known[i+1]:
		#SortingListLetter2.pop(SortingListNum2.index(Known[i]))
		mappingList[1][j] = SortingLetter2[SortingNum2.index(Known[i])]
		del SortingLetter2[SortingNum2.index(Known[i])]
		del SortingNum2[SortingNum2.index(Known[i])]
	    else:
		mappingList[1][j] = SortingLetter2[SortingNum2.index(Known[i])]
	elif i == len(Cipher)-1:
	    #print(SortingNum2)
	    mappingList[0][j] = SortingLetter1[SortingNum1.index(Cipher[i])]	
	    mappingList[1][j] = SortingLetter2[SortingNum2.index(Known[i])]
	i+=1
	j+=1
	
    #print(mappingList)
  
    #return the mapping of n letters
    #example: [a, b, c], [b. a, c], and if c doesnt appear even once, just delete c from the list of mapping
    return mappingList


#main function:
knownTextFile = sys.argv[2]
ciphertextFile = sys.argv[1]

#scan the knownsample textfile to know the most "common" letter of words (get the numebr of letter that occur the most
countLetter = []
x = 0
#e = 0
largestCount = 0
largestCountWordNum = 0
while x < 10:
    countLetter.append(0)
    x += 1
FileKnown = open(knownTextFile, "r")
for line in FileKnown:
    xxx = line.split(" ")
    for i in xxx:
	i = i.lower()
	for iii in i:
	    if iii in listOfLetters:
		#do nothing
		i = i
	    else:
		#print(i.find(iii))
		#print(iii)
		i = i[0:i.find(iii)]
        if len(i) >= 10:
            e = 10
            while e < len(i)+1:
                countLetter.append(0)
                e += 1
        countLetter[len(i)] += 1
        if largestCount < countLetter[len(i)]:
            largestCount = countLetter[len(i)]
	    largestCountWordNum = len(i)

FileKnown.close()
possibleListOf2 = listPossible2()
possibleListOf3 = listPossible3(possibleListOf2)
possibleListOf1 = listOfLetters

indexP = 0
cell = 0
space = ' '
numberOfTime = 1
#largestCountWordNum = 3
while numberOfTime < largestCountWordNum + 1:
    #find the mappings of words/letters starting from the most common number of words
    FinalPossibleList = listPossibleN(numberOfTime, possibleListOf2, possibleListOf3)
    [NumList1, LetterList1] = freqAnalysis(ciphertextFile, FinalPossibleList, numberOfTime)
    [NumList2, LetterList2] = freqAnalysis(knownTextFile, FinalPossibleList, numberOfTime)
    #remove all the letterlist2 cell if contain space
    while cell < len(LetterList2):
	#print(cell)
	if space in LetterList2[cell]:
	    indexP = cell
	    LetterList2.pop(indexP)
	    NumList2.pop(indexP)
	    cell = cell - 1
	cell += 1
    mappingList1 = sortingLists(NumList1, LetterList1, NumList2, LetterList2, numberOfTime)
    if numberOfTime == 1:
	mappingList11 = mappingList1[0]
	mappingList12 = mappingList1[1]
    elif numberOfTime == 2:
	mappingList21 = mappingList1[0]
	mappingList22 = mappingList1[1]
    elif numberOfTime == 3:
	mappingList31 = mappingList1[0]
	mappingList32 = mappingList1[1]
    
    print("FINAL MAPPING LIST: \n")
    print(mappingList1)
    print("\n\n\n\n")
    
    numberOfTime += 1
    del FinalPossibleList[:]
    del NumList1[:]
    del NumList2[:]
    del LetterList1[:]
    del LetterList2[:]
    del mappingList1[:]
print("--- %s seconds ---" % (time.time() - startTime))

markStart = 0
markEnd = 0
check = 3
fileOpen = open(ciphertextFile, "r")
for line in fileOpen:
    while i < len(line):
	if check = 3:
 	    if i+3 < len(line):
	        index3 = line[i:i+largestCountWordNum]
	        if index3 in mappingList31:
	            outputTemp = mappingList32[mappingList31.index(index3)]
		    markEnd = i
	
	if i < len(line)-1:
	    i += 1
	else:
	    i = markStart


	    elif index3[0:2] in mappingList22[0]:
		output += mappingList22[1][mappingList22[0].index(index3[0:2])]
		




   




