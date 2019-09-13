# Python program for implementation of Radix Sort 
  
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10
  
# Driver code to test above 
arr = [ 838, 43, 2345, 234, 12, 34, 21, 663434] 
radixSort(arr) 
  
for i in range(len(arr)): 
    print(arr[i]), 



def freqAnalysis(FileName, possibleList, length):
    j = 0
    aa = len(possibleList)
    #print(aa)
    countingList = [0 for x in range(aa)]
    file = open(FileName, "r")
    for line in file:
        #print line
        i = 0
        while i < len(line)-1:
          gram2 = ''.join(line[i:i+length])
          #print(gram2)
          while j < len(possibleList):
            if gram2 == possibleList[j]:
              #print(countingList[w])
              countingList[j] += 1
              break
            j += 1
          i += 1
          j = 0
    file.close()
    return countingList