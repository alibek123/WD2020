from typing import List

a = int(input())
b: List[int] = []
c = 0
for i in range(a):
    b.append(int(input()))

for i in b:
    first = b[i-1]
    second = b[i]
    third = b[i + 1]
    if second > third and second > first:
        c += 1
print(c)
