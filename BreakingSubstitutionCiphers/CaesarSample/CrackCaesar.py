import sys

listOfLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

CipherFileName = sys.argv[1]
DictionaryFile = sys.argv[2]
CipherStr = ""

fileCipher = open(CipherFileName, "r")
for line in fileCipher:
    for i in line:
	if i.lower() in listOfLetters:
   	    CipherStr += i.lower()
	elif i == ' ':
	    CipherStr += i
    break
fileCipher.close()

i = 0
z = 1
count = 0
TransStr = ""
shiftnum = 0
largestCount = 0
r = 0
while z < 26:
    while i < len(CipherStr):
	if CipherStr[i] in listOfLetters:
	    if listOfLetters.index(CipherStr[i])+z > 25:
		zz = listOfLetters.index(CipherStr[i])+z-26
		TransStr += listOfLetters[zz]
	    else:
                TransStr += listOfLetters[listOfLetters.index(CipherStr[i])+z]
	elif CipherStr[i] == ' ':
	    TransStr += ' '
	i += 1

    fileDictionary = open(DictionaryFile, "r")
    for line in fileDictionary:
	line1 = line[0:(len(line)-1)]
	word = TransStr.split(' ')
	#print(len(word))
	while r < len(word):
	    if word[r] == line1.lower():
	        count += 1
	        break
	    r += 1
    fileDictionary.close()
    TransStr = ""

    if largestCount < count:
        largestCount = count
	shiftnum = z
    count = 0
    z += 1
    i = 0
    r = 0

print(26-shiftnum)
output = ""
fileCipher1 = open(CipherFileName, "r")
for line in fileCipher1:
    for i in line:
	i = i.lower()
	if i in listOfLetters:
	    if listOfLetters.index(i)+shiftnum > 25:
		zz = listOfLetters.index(i)+shiftnum-26
		output += listOfLetters[zz]
	    else:
                output += listOfLetters[listOfLetters.index(i)+shiftnum]
	else:
	    output += i
print(output)
fileCipher1.close()
	    
    
