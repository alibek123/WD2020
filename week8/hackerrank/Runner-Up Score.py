if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(set(arr)))
    arr.pop()
    print(arr[-1])
