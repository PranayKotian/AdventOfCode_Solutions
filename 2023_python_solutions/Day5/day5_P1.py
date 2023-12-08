#Advent of Code 2023: Day 5 Part 1 solution
#Author: Pranay Kotian

import os

total = 0
seeds = []
conversions = []

#Input text modified (titles removed, semicolons used to signify new conversion table)
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text5.txt") as file:
    lines = file.read().splitlines()

seeds = [int(i) for i in lines[0].split()]
conversions = []

for line in lines[1:]:
    if ":" in line:
        conversions.append([])
    else:
        nums = [int(i) for i in line.split()]
        conversions[-1].append((nums[1], nums[1]+nums[2]-1, nums[0]-nums[1]))

for stage in conversions:
    for idx, seed in enumerate(seeds):
        for convert in stage:
            if seed in range(convert[0], convert[1]+1):
                seeds[idx] += convert[2]
                break

print(min(seeds))