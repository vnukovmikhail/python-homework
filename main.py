while True:
    n = input().split(' ')
    s = 0
    for el in n:
        s += int(el)
    print(s/len(n))