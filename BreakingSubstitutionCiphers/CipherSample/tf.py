import sys

file = open(sys.argv[1], "r")
for line in file:
  #print(line)
  str2 = line[1] + line[2]
  print(str2)



file.close()
