def skg(num):
    for i in range(len(num) - 1):
        if(num[i] > num[i+1]): return "NO"
    
    return "YES"

for t in range(int(input())):
    s = input()
    print(skg(s))