def min(a, b, c, d):
    if a >= b:
        min_1 = b
    else:
        min_1 = a
    if c >= d:
        min_2 = d
    else:
        min_2 = c
    if min_1 >= min_2:
        print(min_2)
    else:
        print(min_1)


a = int(input())
b = int(input())
e = int(input())
d = int(input())
min(a, b, e, d)
