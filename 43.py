import math

n, k = [int(i) for i in input().split()]
lower, upper = 10**(k-1), 10**k
for t in range(lower, upper):
    cnt = 0
    if(math.gcd(n,t) == 1):
        print(t, end=' ')
        cnt+=1
    if(cnt == 10):
        print()