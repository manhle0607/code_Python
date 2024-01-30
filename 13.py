def frac(s):
    fractor = 1
    for i in range(1, int(s)+1):
        fractor *= i
    return fractor

def kt(s):
    tong, kq = 0, int(s)
    for i in s:
        tong += frac(int(i))
    if tong != kq:
        return "NO"
    return "YES"     

for t in range(int(input())):
    s = input()
    print(kt(str(s)))
     