a = int(input())
b = []
c = False
for i in range(a):
    b.append(int(input()))

for i in b:
    if b[int(i)] > 0 and b[int(i) - 1] > 0:
        c = True
        break
    elif (b[int(i)] < 0) and (b[int(i) - 1] < 0):
        print("here")
        c = True
        break
    else:
        c = False
if c:
    print("YES")
else:
    print("NO")
