#Advent of Code 2023: Day 14 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text14.txt") as file:
    lines = file.read().splitlines()

lines = [list(line) for line in lines]

ROWS = len(lines)
COLS = len(lines[0])

total = 0
for c in range(COLS):
    bot = 0
    for r in range(ROWS):
        if lines[r][c] == "#":
            bot = r+1
        if lines[r][c] == "O":
            total += COLS - bot
            bot += 1

print(total)