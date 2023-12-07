#Advent of Code 2023: Day 1 Part 2 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "/text1.txt") as file:
    lines = file.readlines()

total = 0
first = ""
last = ""

#inputs are assumed to eventually have a numeric number
#so first and last should always be updated for each line
for line in lines:
  for i in line:
    if i.isnumeric():
      first = i 
      break
  for j in line[::-1]:
    if j.isnumeric():
      last = j
      break
  total += int(first+last)

print(total)