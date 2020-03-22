def front_back(str):
    if len(str) <= 1:
        return str
    str = str[-1] + str[1:-1] + str[0]
    return str


print(front_back("a"))
