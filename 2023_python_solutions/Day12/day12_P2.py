#Advent of Code 2023: Day 12 Part 2 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text12.txt") as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    gear, working = line.split()
    gears = [i for i in gear]
    working = [int(i) for i in working.split(",")]

    allcombos = returncombos(gears, gears.count("#"), sum(working))

    for combo in allcombos:
        if [len(i) for i in combo.split()] == working:
            total += 1

#INCOMPLETE SOLUTION