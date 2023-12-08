#Advent of Code 2023: Day 7 Part 1 solution
#Author: Pranay Kotian

import os
from collections import Counter

#Input text not modified
here = os.path.dirname(os.path.abspath(__file__))
with open(here + "\\text7.txt") as file:
    lines = file.read().splitlines()

total = 0
hands = [[],[],[],[],[],[],[]]
handToBid = {}

for i in range(len(lines)):
  hand,bid = lines[i].split()
  bid = int(bid)
  handToBid[hand] = bid
  handCount = Counter(hand)

  if "J" in handCount:
    jCount = handCount['J']
    del handCount['J']
    if jCount == 5:
      handCount = Counter("AAAAA")
    else:
      handCount[handCount.most_common(1)[0][0]] += jCount
  
  l = len(handCount)
  if l == 1: #five of a kind
    hands[0].append(hand)
  elif l == 2: 
    if handCount.most_common(1)[0][1] == 4: #four of a kind
      hands[1].append(hand)
    else: #full house
      hands[2].append(hand)
  elif l == 3: 
    if handCount.most_common(1)[0][1] == 3: #three of a kind
      hands[3].append(hand)
    else: #two pair
      hands[4].append(hand)
  elif l == 4: #one pair
    hands[5].append(hand)
  else: #l == 5: #high card
    hands[6].append(hand)
  
#https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
alphabet = "AKQT98765432J"
sortedHands = []
for category in hands:
  sortedHands.append(sorted(category, key=lambda word: [alphabet.index(c) for c in word]))

totalLen = 0
total = 0
rank = len(lines)

for category in sortedHands:
  for hand in category:
    total += rank*handToBid[hand]
    rank -= 1

print(total)