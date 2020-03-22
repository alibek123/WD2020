a = int(input())
b = []
num: int = 0
for i in range(a):
    b.append(int(input()))
for i in range(len(b)):
    if b[i] > 0:
        num += 1
print(num)
