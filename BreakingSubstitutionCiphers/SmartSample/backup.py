def sortFreq(List):
    current = 0
    largest = 1
    CCurrent = 0
    temp = 0
    ListofPossible = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    while CCurrent < 27:
        while current < 27:
            if List[largest] < List[current]:
                largest = current
            current += 1
        #print("Largest -> ", List[largest])
        temp = List[CCurrent]
        List[CCurrent] = List[largest]
        List[largest] = temp

        temp = ListofPossible[CCurrent]
        ListofPossible[CCurrent] = ListofPossible[largest]
        ListofPossible[largest] = temp
        CCurrent += 1
        current = CCurrent
        if current < 26:
            largest = current + 1

    return ListofPossible

knownTextFile = sys.argv[2]
ciphertextFile = sys.argv[1]

freqListCipher = freqAnalysis(ciphertextFile)
freqListKnown = freqAnalysis(knownTextFile)
#print(freqListKnown)
#print(freqListCipher)

CompareCipher = sortFreq(freqListCipher)
CompareKnown = sortFreq(freqListKnown)
#print(CompareCipher)
#print(CompareKnown)

with open(ciphertextFile, "r+") as File:
    for line in File:
        decrpyted = []
        z = 0
        while z < len(line):
            decrpyted.append('')
            z += 1
        w = 0
        for xx in line:
            if xx == '\n':
                continue
            xx = xx.lower()
            i = 0
            check = 0
            while i < 27:
                if xx == CompareCipher[i]:
                    check = 1
                    decrpyted[w] = CompareKnown[i]
                    break
                i += 1
            if check == 0:
                decrpyted[w] = xx
            w += 1
        print(''.join(map(str, decrpyted)))
File.close()



def freqAnalysis(FileName):
    listOfLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    aa = 27
    i = 0
    j = 0
    w = 0
    z = 0
    count3 = 0
    possibleList3 = [[[0 for x in range(aa)] for y in range(aa)] for z in range(aa)]
    while i < 27:
        possibleList3.append(000)
        while j < 27:
            while k < 27:
                possibleList3[i][j][k] = possibleList[i][j]+listOfLetters[k]
                count3 += 1
                k += 1
            j += 1
            k = 0
        i += 1
        j = 0


    print("count3 = ", count3)
    #print(possibleList3)
    aa = 27
    
    countingList = [[0 for x in range(aa)] for y in range(aa)]
    file = open(FileName, "r")
    for line in file:
        #print line
        i = 0
        while i < len(line)-1:
          gram2 = line[i].lower()+line[i+1].lower()
          j = 0
          #print(gram2)
          while j < 27:
            k = 0
            while k < 27:
              #print(i)
              if gram2 == possibleList[j][k]:
                #print(countingList[w])
                countingList[j][k] += 1
                break
              k += 1
            j += 1
          i += 1
    file.close()
    return countingList
