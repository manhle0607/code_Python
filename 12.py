import math

def kt1(s):
    if s < 2:
        return False
    for i in range(2, int(math.sqrt(s)) + 1):
        if(s%i==0):
            return False
    return True 

def kt2(s):
    sum = 0
    for i in s:
        if(not kt1(int(i))):
            return "NO"
        sum += int(i)
    num1, num2 = s, s[::-1]
    if not kt1(sum) or not kt1(int(num1)) or not kt1(int(num2)):
        return "NO"
    return "YES"

for t in range(int(input())):

    print(kt2(input()))
        
        