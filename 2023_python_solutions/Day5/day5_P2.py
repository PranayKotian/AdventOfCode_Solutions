#Advent of Code 2023: Day 5 Part 2 solution
#Author: Pranay Kotian

import os

total = 0
seeds = []
conversions = []

#Input text modified (titles removed, semicolons used to signify new conversion table)
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text5.txt") as file:
    lines = file.read().splitlines()

raw = lines[0].split()
seeds = []
for i in range(0,len(raw),2):
  start = int(raw[i])
  length = int(raw[i+1]) #number of vals in range (including start val)
  seeds.append((start, start+length-1)) #adds (start,end) range

for line in lines[1:]:
  if ":" in line:
    conversions.append([])
  else:
    nums = [int(i) for i in line.split()]
    conversions[-1].append((nums[1], nums[1]+nums[2]-1, nums[0]-nums[1]))

valAdded = False
new = []
for stage in conversions:
  while seeds:
    s1,s2 = seeds.pop()
    
    for c1,c2,add in stage:
      if s1 <= c2 and c1 <= s2: #checks if ranges overlap at all
        valAdded = True
        if s1 >= c1 and s2 <= c2: #seed range fully within convert range
          new.append((s1+add,s2+add))
        elif s1 < c1 and s2 > c2: #convert range fully within seed range (some seeds on both ends not converted)
          new.append((c1+add,c2+add))
          seeds.append((s1,c1-1))
          seeds.append((c2+1,s2))
        elif s1 in range(c1,c2+1): #seed range partially within convert range
          new.append((s1+add, c2+add))
          seeds.append((c2+1,s2))
        elif s2 in range(c1,c2+1): #seed range partially within convert range
          new.append((c1+add,s2+add))
          seeds.append((s1,c1-1))
    
    if valAdded == False:
      new.append((s1,s2))
    valAdded = False

  seeds = new
  new = []

#min(seeds) will find the min based on the first value of the range (s1,s2)
print(min(seeds)[0])