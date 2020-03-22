import math

a = int(input())
i = 1
while i <= math.floor(math.sqrt(a)):
    print(i * i)
    i = i + 1
