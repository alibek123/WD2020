import math

a = int(input())
num = 0
for i in range(1, int(math.sqrt(a))):
    if a % i == 0:
        num += 1
num *= 2
if a % math.sqrt(a) == 0:
    num += 1
print(num)
