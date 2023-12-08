#Advent of Code 2023: Day 8 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text8.txt") as file:
    lines = file.read().splitlines()

instruc = lines[0]
mappings = {}
starts = []
ends = []

for line in lines[1:]:
    key, LR = line.split(" = ")
    L, R = LR.split()
    mappings[key] = (L,R)
    if key[2] == "A":
        starts.append(key)
    if key[2] == "Z":
        ends.append(key)

moves = 0
minmoves = []

for idx, start in enumerate(starts):
    moves = 0
    while True:
        c = instruc[moves%len(instruc)]
        if c == "R":
            starts[idx] = mappings[starts[idx]][1]
        else:# c == "L":
            starts[idx] = mappings[starts[idx]][0]
        moves += 1
        if starts[idx][2] == "Z":
            minmoves.append(moves)
            break

print(minmoves)