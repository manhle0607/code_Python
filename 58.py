import math

def snt(s):
    if int(s) < 2:
        return False
    for i in range(2, int(math.sqrt(s) + 1)):
        if(s % i == 0):
            return False
    return True

def kt(s):
    tong = sum(int(i) for i in s)
    return "YES" if snt(tong) else "NO"

for t in range(int(input())):
    s = input()
    print(kt(s))