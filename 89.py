import math
t = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(len(a)):
    for j in range(i+1, len(a), 1):
        if math.gcd(a[i], a[j]) == 1:
            print(str(a[i]) + " " + str(a[j]))