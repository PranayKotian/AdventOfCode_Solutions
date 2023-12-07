#Advent of Code 2023: Day 3 Part 2 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "/text3.txt") as file:
    lines = file.read().splitlines()

numbag = set(['1','2','3','4','5','6','7','8','9','0'])

ROWS = len(lines)
COLS = len(lines[0])
total = 0

def search(r,c):
  global total
  
  searchvals = set([(r-1,c-1),(r-1,c),(r-1,c+1),(r,c+1),(r,c-1),(r+1,c+1),(r+1,c),(r+1,c-1)])
  
  nums = []
  addToTot = 1
  while searchvals:
    a,b = searchvals.pop()
    if a < 0 or b < 0 or a >= ROWS or b >= COLS or lines[a][b] not in numbag:
      continue
    l = b
    r = b
    while l >= 0 and lines[a][l] in numbag:
      l -= 1
    while r < COLS and lines[a][r] in numbag:
      r += 1
    
    stringToAdd = ""
    for colval in range(l+1, r):
      if (a,colval) in searchvals: searchvals.remove((a,colval))
      stringToAdd += lines[a][colval]
    num = (int(stringToAdd))
    
    nums.append(num)
    addToTot *= num

  if len(nums) == 2:
    total += addToTot
      
for r,row in enumerate(lines):
  for c, val in enumerate(row):
    if val == "*":
      search(r,c)

print(total)