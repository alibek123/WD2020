def round_sum(a, b, c):
    if (a and b and c) <= 10:
        return round10(a + b + c)
    else:
        return round10(a) + round10(b) + round10(c)


def round10(num):
    if num % 10 < 5:
        num = int(num / 10) * 10
    else:
        num = (int(num / 10) + 1) * 10
    return num
