def kt(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True   

for t in range(int(input())):
    s = int(input())
    for i in range(22,s,2):
        if kt(str(i)):
            print(i,end=" ")
    print()