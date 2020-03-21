a = int(input())
if a==1:
    print("YES")
while a > 1:
    a = a / 2
    if a == 1:
        print("YES")
    elif a < 1:
        print("NO")
