def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string


if __name__ == '__main__':
    print(mutate_string("abracadabra", 5, "k"))
