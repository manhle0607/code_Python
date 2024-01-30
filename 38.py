import math

for t in range(int(input())):
    s = int(input())
    res = '1'
    for i in range(2, int(math.sqrt(s) + 1)):
        cnt = 0
        while s % i == 0:
            cnt+=1
            s/=i
        if(cnt!=0):
            res += " * " + str(i) + "^" + str(cnt)
        if(s==1):
            break
    if(s!=1): res += " * " + str(int(s)) +"^1"
    print(res) 
        