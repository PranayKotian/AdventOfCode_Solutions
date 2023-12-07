import sys

total = 0
arr = []
for i in range(140):
  line = sys.stdin.readline()
  arr.append(list(line)[0:140])

numbag = set(['1','2','3','4','5','6','7','8','9','0'])

ROWS = len(arr)
COLS = len(arr[0])

def search(r,c):
  global total
  
  searchvals = [(r-1,c-1),(r-1,c),(r-1,c+1),(r,c+1),(r,c-1),(r+1,c+1),(r+1,c),(r+1,c-1)]
  
  numset = set()
  
  addToTot = 1
  for a,b in searchvals:
    if a < 0 or b < 0 or a >= ROWS or b >= COLS or arr[a][b] not in numbag:
      continue
    l = b
    r = b
    while l >= 0 and arr[a][l] in numbag:
      l -= 1
    while r < COLS and arr[a][r] in numbag:
      r += 1
    
    stringToAdd = ""
    for colval in range(l+1, r):
      stringToAdd += arr[a][colval]
    num = (int(stringToAdd))
    if num not in numset:
      numset.add(num)
      addToTot *= (int(stringToAdd))

  if len(numset) == 2:
    total += addToTot
      
for r,row in enumerate(arr):
  for c, val in enumerate(row):
    if val == "*":
      search(r,c)

print(total)