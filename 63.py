import math

def snt(n):
    if int(n) < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

def kt(s):
    for i in range(len(s)):
        if snt(i) and (int(s[i]) != 2 or int(s[i]) != 3 or int(s[i]) != 5 or int(s[i]) != 7):
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(kt(s))