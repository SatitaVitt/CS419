def fA(str):
  letters = "abcdefgh"
  letter = []
  z = 0
  while z < len(letters):
    
  count = []
  msg = ''
  w = 0
  for i in range(8):
    count.append(0)
  i = 0
  for i in str:
    msg += i
    
    if i in letter:
      count[letter.find(i)] += 1
  return count, msg

letter = "abcdefgh"
str = "aaaaaaaaabbbbcccfffgh"
str2 = "aabcccccccccfgggh"

[freList1, msg] = fA(str)
[freList2, plain] = fA(str2)

print("freList1:")
print(freList1)
print("msg")
print(msg)

compare1 = sorted(freList1)
compare2 = sorted(freList2)
print(compare1)
print(compare2)

return1 = ''
for i in msg:
  if i in letter:
    return1 += letter[freList2.index(compare2[compare1.index(freList1[letter.find(i)])])]

print(return1)


