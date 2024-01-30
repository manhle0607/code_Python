import math

def snt(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if(a % i == 0): return False
        
    return a > 1

for t in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1,n):
        if(math.gcd(n,i)) == 1:
            k += 1
    if(snt(k)):
        print("YES")
    else: print("NO")