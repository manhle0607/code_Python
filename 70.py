def tb(a,b):
    for i in range(len(a)):
        if abs(ord(a[i]) - ord(a[i-1])) != abs(ord(b[i]) - ord(b[i-1])):
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    s1 = s[::-1]
    print(tb(s,s1))