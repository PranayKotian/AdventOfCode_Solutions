#Advent of Code 2023: Day 10 Part 1 solution
#Author: Pranay Kotian

import os

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text10.txt") as file:
    lines = file.read().splitlines()

topcons = set(["|", "7", "F"])
botcons = set(["|", "L", "J"])
rgtcons = set(["-", "J", "7"])
lftcons = set(["-", "L", "F"])

# dirs = {
#     "|": [(-1,0), (1,0)],
#     "-": [(0,-1), (0,1)],
#     "L": [(-1,0), (0,1)],
#     "J": [(0,-1), (-1,0)],
#     "7": [(0,-1), (1,0)],
#     "F": [(1,0), (0,1)]
# }

pipetodir = {
("|", "U"): "U",
("|", "D"): "D",
("-", "L"): "L",
("-", "R"): "R",
("L", "D"): "R",
("L", "L"): "U",
("J", "D"): "L",
("J", "R"): "U",
("7", "U"): "L",
("7", "R"): "D",
("F", "U"): "R",
("F", "L"): "D"
}

dirtocoords = {
    "U": (-1,0),
    "D": (1,0),
    "L": (0,-1),
    "R": (0,1)
}

#Find position of S
s = [0,0]
for l, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "S":
            s = (l, c)
            break

startPipes = []
#Find connecting pipes to S:
if lines[s[0]-1][s[1]] in topcons:
    startPipes.append([(s[0]-1,s[1]), "U"])
if lines[s[0]+1][s[1]] in botcons:
    startPipes.append([(s[0]+1,s[1]), "D"])
if lines[s[0]][s[1]+1] in rgtcons:
    startPipes.append([(s[0],s[1]+1), "R"])
if lines[s[0]][s[1]-1] in lftcons:
    startPipes.append([(s[0],s[1]-1), "L"])

p1,p2 = startPipes

steps = 1
while p1[0] != p2[0]:
    print(f"{p1} {p2}")
    p1tile = lines[p1[0][0]][p1[0][1]]
    p1dir = p1[1]
    p1nextdir = pipetodir[(p1tile, p1dir)]
    p1[0] = [p1[0][0] + dirtocoords[p1nextdir][0], p1[0][1] + dirtocoords[p1nextdir][1]]
    p1[1] = p1nextdir

    p2tile = lines[p2[0][0]][p2[0][1]]
    p2dir = p2[1]
    p2nextdir = pipetodir[(p2tile, p2dir)]
    p2[0] = [p2[0][0] + dirtocoords[p2nextdir][0], p2[0][1] + dirtocoords[p2nextdir][1]]
    p2[1] = p2nextdir

    steps += 1

print(steps)