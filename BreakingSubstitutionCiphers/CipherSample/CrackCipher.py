import sys

def freqAnalysis(FileName):
    possibleList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    countingList = []
    w = 0
    while w < 27:
        countingList.append(0)
        w += 1
    file = open(FileName, "r")

    for line in file:
        #line = line.lower()
        #print line
        for x in line:
            x = x.lower()
            i = 0
            while i < 27:
                if x == possibleList[i]:
                    countingList[i] += 1
                    break
                i += 1
    file.close()
    return countingList

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
with open(ciphertextFile, "r") as File:
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
