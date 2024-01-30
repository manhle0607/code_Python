def kt(s):
    for i in s:
        if(s[len(s)-1] != '6' or s[len(s)-2]!='8'):
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(kt(s))
    