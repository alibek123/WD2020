import math

a = int(input())
i = a
c = 0
while i > 1:
    if a % i == 0:
        c = i
    i -= 1
print(c)
