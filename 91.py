import math

def snt(s):
    if int(s) < 2:
        return False
    for i in range(2, int(math.sqrt(s) + 1)):
        if s % i == 0:
            return False
    return s >= 2
    

s = int(input())
a = [int(i) for i in input().split()]
lst = {}
for i in a:
    if snt(i):
        if i in lst:
            lst[i] += 1
        else:
            lst[i] = 1

for i in lst:
    print(str(i) + " " + str(lst[i]))
     
