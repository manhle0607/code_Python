import math

def snt(s):
    for i in range(2, int(math.sqrt(s) + 1)):
        if(s % i == 0):
            return False
    return s >= 2

for i in range(int(input())):
    s = input()
    print("YES" if snt(int(s[0:3])) and snt(int(s[-3:])) else "NO")