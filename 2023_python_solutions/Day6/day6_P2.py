#Advent of Code 2023: Day 6 Part 2 solution
#Author: Pranay Kotian

import os

#Input text modified and shortened to two input numbers
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text6_P2.txt") as file:
    lines = file.read().splitlines()

total = 0
time = int(lines[0]) #time alloted
dist = int(lines[1]) #distance to beat

#distance = speed * time
#speed = timeHeld 
#time = timAlloted - timeHeld
#distance = timeHeld * (timAlloted - timeHeld)

minHold = 208141212571410
#Binary search for minimum hold time
l = 1
r = 46857582
while l <= r: #hold time m valid and m-1 not valid
  m = (l+r)//2
  mWorks = m * (time-m) > dist
  mm1Works = (m-1) * (time-(m-1)) > dist
  
  if mWorks and not mm1Works:
    minHold = m
    break
  elif mWorks and mm1Works:
    r = m-1
  else: 
    l = m+1

maxHold = 0
#Binary search for maximum hold time
l = 0
r = 46857581
while l <= r: #hold time m valid and m+1 not valid
  m = (l+r)//2
  mWorks = m * (time-m) > dist
  mp1Works = (m+1) * (time-(m+1)) > dist
  
  if mWorks and not mp1Works:
    maxHold = m
    break
  elif mWorks and mp1Works:
    l = m+1
  else: #not mWorks and not m1Works
    r = m-1

print(maxHold-minHold+1) #Ways to beat the record