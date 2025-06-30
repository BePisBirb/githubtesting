import math

def median(input):
  input.sort()
  if len(input) % 2 == 0:
    return (input[math.floor((len(input) / 2) - 1)] + input[math.floor(len(input)/2)]) / 2
  else:
    return input[math.floor(len(input) / 2)]

print(median([0, 3, 5, 7, 10, 11, 32, 87, 100, 999]))