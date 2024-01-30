n = int(input())
s = [int(i) for i in input().split()]
cnt = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] > s[j]:
            cnt += 1
print(cnt)