def kt(n):
    if len(n) < 3:
        return "NO"
    arr = list(int(i) for i in n)
    up = True
    for i in range(1, len(arr)):
        if up and arr[i] <= arr[i-1]:
            up = False
        elif not up and arr[i] >= arr[i-1]:
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(kt(s))
        