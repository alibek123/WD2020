def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i - 1] == 'h' and str[i] == 'i':
            count += 1
    return count
