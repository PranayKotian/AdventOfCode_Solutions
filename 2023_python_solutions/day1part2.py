import sys

numbers = {
  'one': "1",
  'two': "2",
  'three': "3",
  'four': "4",
  'five': "5",
  'six': "6",
  'seven': "7",
  'eight': "8",
  'nine': "9"
}

numbersrev = {k[::-1]:v for k,v in numbers.items()}

total = 0
for i in range(1000):
  name = sys.stdin.readline()
  for idx,i in enumerate(name):
    if i.isnumeric():
      first = i 
      break
    if name[idx:idx+3] in numbers:
      first = numbers[name[idx:idx+3]]
      break
    if name[idx:idx+4] in numbers:
      first = numbers[name[idx:idx+4]]
      break
    if name[idx:idx+5] in numbers:
      first = numbers[name[idx:idx+5]]
      break
  backname = name[::-1]

  for idx,j in enumerate(backname):
    if j.isnumeric():
      last = j
      break
    if backname[idx:idx+3] in numbersrev:
      last = numbersrev[backname[idx:idx+3]]
      break
    if backname[idx:idx+4] in numbersrev:
      last = numbersrev[backname[idx:idx+4]]
      break
    if backname[idx:idx+5] in numbersrev:
      last = numbersrev[backname[idx:idx+5]]
      break
  
  total += int(first+last)

print(total)