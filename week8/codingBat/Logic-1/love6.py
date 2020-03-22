def love6(a, b):
    if (abs(a - b) or abs(b - a)) == 6:
        return True
    elif (a == 6 or b == 6) or a + b == 6:
        return True
    return False
