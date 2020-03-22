import math

a = int(input())
while True:
    if math.log(a, 2).is_integer():
        print(int(math.log(a, 2)))
        break
    a += 1
