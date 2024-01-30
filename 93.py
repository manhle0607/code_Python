def tich(s):
    kq = 1
    for i in s:
        kq *= int(i)
    return kq

for t in range(int(input())):
    s = int(input())
    a = input().split()
    a.sort(key = lambda s: (tich(s), int(s)))
    print(*a)

