def make_chocolate(small, big, goal):
    max = goal / 5

    if big >= max:
        if small >= (goal - 5 * max):
            return goal - 5 * max
    if big < max:
        if small >= (goal - 5 * big):
            return goal - 5 * big
    return -1
