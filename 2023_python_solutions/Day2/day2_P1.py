#Advent of Code 2023: Day 2 Part 1 solution
#Author: Pranay Kotian

import os

#Input text modified:
# "Game " removed from beginning of each line
# Semicolons (;) replaced with commas (,) since individual subsets were irrelevant
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "/text2.txt") as file:
    lines = file.readlines()

total = 0
for name in lines:
  namesplit = name.split(":")
  
  ID = int(namesplit[0])
  groups = namesplit[1].split(', ')
  minGreen = 0
  minRed = 0
  minBlue = 0
  
  #Future change: shorten code with if all() statement
  addVal = True
  for i in groups:
    count,color = i.split()
    count = int(count)
    if count > 14 or (color == "green" and count > 13) or (color == "red" and count > 12):
      addVal = False
      break

  if addVal:
    total += ID
    
print(total)