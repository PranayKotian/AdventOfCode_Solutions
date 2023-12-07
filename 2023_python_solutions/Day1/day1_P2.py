#Advent of Code 2023: Day 1 Part 2 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "/text1.txt") as file:
    lines = file.readlines()

numbers = {
  'one': "1",
  'two': "2",
  'three': "3",
  'four': "4",
  'five': "5",
  'six': "6",
  'seven': "7",
  'eight': "8",
  'nine': "9"
}
numbersrev = {k[::-1]:v for k,v in numbers.items()}

total = 0

#inputs are assumed to eventually have a numeric or text-based number
#otherwise, both loops would run into indexOutOfRange errors
for line in lines:
  for idx,i in enumerate(line):
    if i.isnumeric():
      first = i 
      break
    if line[idx:idx+3] in numbers:
      first = numbers[line[idx:idx+3]]
      break
    if line[idx:idx+4] in numbers:
      first = numbers[line[idx:idx+4]]
      break
    if line[idx:idx+5] in numbers:
      first = numbers[line[idx:idx+5]]
      break
  nameRev = line[::-1]

  for idx,j in enumerate(nameRev):
    if j.isnumeric():
      last = j
      break
    if nameRev[idx:idx+3] in numbersrev:
      last = numbersrev[nameRev[idx:idx+3]]
      break
    if nameRev[idx:idx+4] in numbersrev:
      last = numbersrev[nameRev[idx:idx+4]]
      break
    if nameRev[idx:idx+5] in numbersrev:
      last = numbersrev[nameRev[idx:idx+5]]
      break
  
  total += int(first+last)

print(total)