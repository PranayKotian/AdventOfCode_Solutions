#Advent of Code 2023: Day 4 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "/text4.txt") as file:
    lines = file.read().splitlines()

arr = [line.split(": ")[1] for line in lines]

points = 0
for a in arr:
    winners, picks = a.split(" | ")
    winners = set([int(i) for i in winners.split()])
    picks = set([int(i) for i in picks.split()])

    wins = 0
    for p in picks:
        if p in winners:
            wins += 1
    
    if wins != 0:
        points += 2**(wins-1)

print(points)