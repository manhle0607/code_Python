import math

def snt(s):
    for i in range(2, int(math.sqrt(s) + 1)):
        if s % i == 0:
            return False
    return s >= 2

def kt(s):
    if not snt(len(s)):
        return "NO"
    cnt = 0
    for i in s:
        if snt(int(i)):
            cnt += 1
    if cnt <= len(s) - cnt:
        return "NO"
    return "YES"

for i in range(int(input())):
    s = input()
    print(kt(str(s)))