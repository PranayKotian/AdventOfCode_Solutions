#Advent of Code 2023: Day 8 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text8.txt") as file:
    lines = file.read().splitlines()

instruc = lines[0]
mappings = {}

for line in lines[1:]:
    key, LR = line.split(" = ")
    L, R = LR.split()
    mappings[key] = (L,R)

start = "AAA"
moves = 0

while True:
    c = instruc[moves%len(instruc)]
    if c == "R":
        start = mappings[start][1]
    else:# c == "L":
        start = mappings[start][0]
    moves += 1
    if start == "ZZZ":
        print(moves)
        break