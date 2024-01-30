import math

def snt(s):
    if int(s) < 2:
        return "NO"
    for i in range(2, int(math.sqrt(s) + 1)):
        if(s % i == 0):
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(snt(int(s[-4:])))