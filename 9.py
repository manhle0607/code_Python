for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    list = input().split()
    print(*(list[b:] + list[:b]))
    