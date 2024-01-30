def kt(n):
    if sum(int(i) for i in n) % 10 != 0:
        return "NO"
    for i in range(len(n)-1):
        if abs(ord(n[i]) - ord(n[i+1])) != 2:
            return "NO"
    return "YES"

for t in range(int(input())):
    n = input()
    print(kt(n))
    
    