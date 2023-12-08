#Advent of Code 2023: Day 4 Part 2 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "/text4.txt") as file:
    lines = file.read().splitlines()

arr = [line.split(": ")[1] for line in lines]
cards = [1 for i in range(len(arr))]

points = 0
for idx,a in enumerate(arr):
    winners, picks = a.split(" | ")
    winners = set([int(i) for i in winners.split()])
    picks = set([int(i) for i in picks.split()])

    wins = 0
    for p in picks:
        if p in winners:
            wins += 1
    
    for i in range(idx+1, min(len(arr), idx+1+wins)):
        cards[i] += cards[idx]

print(sum(cards))