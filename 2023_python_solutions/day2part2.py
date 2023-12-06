import sys

total = 0
for i in range(100):
  name = sys.stdin.readline()
  namesplit = name.split(":")
  
  ID = int(namesplit[0])
  groups = namesplit[1].split(', ')
  minGreen = 0
  minRed = 0
  minBlue = 0
  
  for i in groups:
    two = i.split()
    if two[1] == "green":
      minGreen = max(minGreen, int(two[0]))
    elif two[1] == "blue":
      minBlue = max(minBlue, int(two[0]))
    elif two[1] == "red":
      minRed = max(minRed, int(two[0]))
    
  total += minGreen * minBlue * minRed
    
print(total)