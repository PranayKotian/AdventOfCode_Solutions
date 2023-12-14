#Advent of Code 2023: Day 13 Part 1 solution
#Author: Pranay Kotian

import os
import numpy

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text13.txt") as file:
    lines = file.read().splitlines()

arr = [[]]
for line in lines:
    if line == "":
        arr.append([])
    else:
        arr[-1].append(list(line))

total = 0
for idx, pattern in enumerate(arr):
    ROWS = len(pattern)
    COLS = len(pattern[0])

    for i in range(1,COLS):
        minDist = min(i, COLS-i)

        validMirror = True
        for r in range(ROWS):
            if pattern[r][i-minDist:i] != pattern[r][i:i+minDist][::-1]:
                validMirror = False
                break
        
        if validMirror:
            total += i
            break
    
    if validMirror == False:
        pattern = numpy.array(arr[idx]).T.tolist()
        ROWS = len(pattern)
        COLS = len(pattern[0])
        for i in range(1,COLS):
            minDist = min(i, COLS-i)

            validMirror = True
            for r in range(ROWS):
                if pattern[r][i-minDist:i] != pattern[r][i:i+minDist][::-1]:
                    validMirror = False
                    break
            
            if validMirror:
                total += 100*i
                break

print(total)