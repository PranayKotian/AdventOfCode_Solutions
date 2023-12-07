import sys 

total = 0

seeds = []
conversions = [[], [], [], [], [], [], []]
conversionTableCounter = 0
for i in range(205):
  name = sys.stdin.readline()[:-1] 
  
  if i == 0:
    raw = name.split()
    seeds = [(int(raw[i]),int(raw[i])+int(raw[i+1])-1) for i in range(0,len(raw),2)]
  else:
    if name == ":":
      conversionTableCounter += 1
    else:
      nums = [int(i) for i in name.split()]
      conversions[conversionTableCounter].append((nums[1], nums[1]+nums[2]-1, nums[0]-nums[1]))

valAdded = False
new = []
for stage in conversions:
  while seeds:
    s1,s2 = seeds.pop()
    
    for c1,c2,add in stage: #some overlap
      if s1 <= c2 and c1 <= s2: #checks if ranges overlap
        valAdded = True
        if s1 >= c1 and s2 <= c2:
          new.append((s1+add,s2+add))
        elif s1 < c1 and s2 > c2:
          new.append((c1+add,c2+add))
          seeds.append((s1,c1-1))
          seeds.append((c2+1,s2))
        elif s1 in range(c1,c2+1):
          new.append((s1+add, c2+add))
          seeds.append((c2+1,s2))
        elif s2 in range(c1,c2+1): 
          new.append((c1+add,s2+add))
          seeds.append((s1,c1-1))
    
    if valAdded == False:
      new.append((s1,s2))
    valAdded = False

  seeds = new
  new = []

print(min(seeds))