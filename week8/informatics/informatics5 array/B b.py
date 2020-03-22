a = int(input())
b = []
for i in range(a):
    c = int(input())
    b.append(c)

for i in range(0,len(b)-1):
    if b[i] % 2 == 0:
        print(b[i])
