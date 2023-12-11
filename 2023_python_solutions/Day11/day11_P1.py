#Advent of Code 2023: Day 11 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text11.txt") as file:
    lines = file.read().splitlines()

ROWS = len(lines)
COLS = len(lines[0])

emptyRows = set([r for r in range(ROWS)])
emptyCols = set([c for c in range(COLS)])
stars = []

for r in range(ROWS):
    for c in range(COLS):
        if lines[r][c] == "#":
            stars.append((r,c))
            if r in emptyRows: emptyRows.remove(r)
            if c in emptyCols: emptyCols.remove(c)

res = 0
for i in range(len(stars)):
    for j in range(i+1,len(stars)):
        ir, ic = stars[i]
        jr, jc = stars[j]
        res += abs(jr-ir) + abs(jc-ic)
        for row in emptyRows:
            if row in range(ir,jr) or row in range(jr,ir):
                res += 1
        for col in emptyCols:
            if col in range(ic,jc) or col in range(jc,ic):
                res += 1

print(res)