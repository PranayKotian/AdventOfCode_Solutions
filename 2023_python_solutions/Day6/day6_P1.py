#Advent of Code 2023: Day 6 Part 1 solution
#Author: Pranay Kotian

import os

#Input text modified (Time and Distance labels removed)
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text6_P1.txt") as file:
    lines = file.read().splitlines()

times = [int(i) for i in lines[0].split()]
dists = [int(i) for i in lines[1].split()]

marginOfError = 1
for idx,t in enumerate(times):
    waysToBeat = 0
    for i in range(t+1):
        if i * (t-i) > dists[idx]:
            waysToBeat += 1
    marginOfError *= waysToBeat

print(marginOfError)