def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif 13 == b:
        return a
    elif 13 == c:
        return a + b
    else:
        return a + b + c
