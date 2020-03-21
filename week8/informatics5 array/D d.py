a = int(input())
b = []
num = 0
for i in range(a):
    b.append(int(input()))
for i in range(len(b)):
    if b[i] > b[i - 1]:
        num += 1
print(num)