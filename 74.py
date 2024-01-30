import math

def snt(s):
    if int(s) < 2:
        return False
    for i in range(2, int(math.sqrt(s) + 1)):
        if(s % i == 0):
            return False
    return True

def kt(s):
    sum = 0
    for i in range(2, int(math.sqrt(s) + 1)):
        while s % i == 0:
            if s % i == 0: 
                sum += int(s[i])
    return sum

for i in  range(int(input())):
    s = int(input())
    
    