def kt(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

for t in range(int(input())):
    s = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    print(kt(a,b))