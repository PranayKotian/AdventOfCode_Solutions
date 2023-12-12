#Advent of Code 2023: Day 12 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text12.txt") as file:
    lines = file.read().splitlines()

def returncombos(arr,curGears,maxGears):
    if "?" not in arr:
        return ["".join(arr)]
    if curGears > maxGears:
        return []
    
    idx = arr.index("?")
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr1[idx] = "."
    arr2[idx] = "#"

    return returncombos(arr1, curGears, maxGears) + returncombos(arr2, curGears+1, maxGears)

total = 0
for line in lines:
    gear, working = line.split()
    gears = [i for i in gear]
    working = [int(i) for i in working.split(",")]

    allcombos = returncombos(gears, gears.count("#"), sum(working))

    for combo in allcombos:
        if [len(i) for i in combo.replace(".", " ").split()] == working:
            total += 1

print(total)