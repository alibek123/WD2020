def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str)):
        if str[i] == 't' and str[i - 1] == 'a' and str[i - 2] == 'c':
            count_cat += 1
    for i in range(len(str)):
        if str[i] == 'g' and str[i - 1] == 'o' and str[i - 2] == 'd':
            count_dog += 1
    return count_dog == count_cat
