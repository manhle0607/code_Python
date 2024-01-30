import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return True

def kt(s):
    cnt = 0
    cnt1 = 0
    for i in s:
        cnt+=1
        if snt(int(i)):
            cnt1+=1
    return "YES" if snt(cnt) and cnt1 > len(s) - cnt1 else "NO"


for t in range(int(input())):
    s = input()
    print(kt(s))
        