import math

a = int(input())
b = int(input())

for i in range(a, b + 1):
    j = int(math.sqrt(i))
    if math.pow(j, 2) == i:
        print(i)
