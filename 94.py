import math

def snt(s):
    if int(s) < 2:
        return 0
    for i in range(2, int(math.sqrt(s)) + 1):
        if s % i == 0:
            return 0
    return 1    

n,m = [int(i) for i in input().split()]
for i in range(n):
    a = [snt(int(i)) for i in input().split()]
    print(*a)

        
