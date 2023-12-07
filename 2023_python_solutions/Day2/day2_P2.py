#Advent of Code 2023: Day 2 Part 2 solution
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