#Advent of Code 2023: Day 14 Part 2 solution
#Author: Pranay Kotian

#VALID solution but too inefficient
import os
import numpy as np

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text14.txt") as file:
    lines = file.read().splitlines()

lines = np.array([list(line) for line in lines])
empty = np.array(lines)
empty[empty == "O"] = "."
temp = empty.copy()

# for l in range(len(empty)):
#     for c in range(len(empty[l])):
#         if empty[l][c] == "O":
#             empty[l][c] = "."

ROWS = len(lines)
COLS = len(lines[0])

cycles = 1000000000
for i in range(cycles):
    start = lines.copy()
    #North
    for c in range(COLS):
        top = 0
        for r in range(ROWS):
            if lines[r][c] == "#":
                top = r+1
            if lines[r][c] == "O":
                temp[top][c] = "O"
                top += 1
    lines = temp.copy()
    temp = empty.copy()

    #West
    for r in range(ROWS):
        left = 0
        for c in range(COLS):
            if lines[r][c] == "#":
                left = c+1
            if lines[r][c] == "O":
                temp[r][left] = "O"
                left += 1
    lines = temp.copy()
    temp = empty.copy()

    #South
    for c in range(COLS):
        bot = ROWS-1
        for r in range(ROWS-1,-1,-1):
            if lines[r][c] == "#":
                bot = r-1
            if lines[r][c] == "O":
                temp[bot][c] = "O"
                bot -= 1
    lines = temp.copy()
    temp = empty.copy()

    #East
    for r in range(ROWS):
        right = COLS-1
        for c in range(COLS-1,-1,-1):
            if lines[r][c] == "#":
                right = c-1
            if lines[r][c] == "O":
                temp[r][right] = "O"
                right -= 1
    lines = temp.copy()
    temp = empty.copy()
    compare = start == lines
    if compare.all():
        break

total = 0
for c in range(COLS):
    top = 0
    for r in range(ROWS):
        if lines[r][c] == "#":
            top = r+1
        if lines[r][c] == "O":
            total += COLS - top
            top += 1
print(total)