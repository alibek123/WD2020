def close_far(a, b, c):
    cond1 = abs(a - b) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2
    cond2 = abs(a - c) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2
    return cond1 or cond2
