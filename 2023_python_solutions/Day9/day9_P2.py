#Advent of Code 2023: Day 9 Part 2 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text9.txt") as file:
    lines = file.read().splitlines()

arr = []
for line in lines:
    arr.append([[int(i) for i in line.split()][::-1]])

    while not all([i==0 for i in arr[-1][-1]]):
        arr[-1].append([arr[-1][-1][i] - arr[-1][-1][i+1] for i in range(len(arr[-1][-1])-1)]) 
    arr[-1][-1].append(0)

for block in arr:
    for i in range(len(block)-2, -1, -1):
        block[i].append(block[i][-1]-block[i+1][-1])

total = 0
for block in arr:
    total += block[0][-1]
print(total)