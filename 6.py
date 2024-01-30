for t in range(int(input())):
    n = int(input())
    s = [int(i) for i in input().split()]
    s.sort()
    cnt = 0
    for i in range(len(s) - 2):
        left, right = i+1, len(s) - 1
        while(left < right):
            cur = int(s[i]) + int(s[left]) + int(s[right])
            if cur == 0:
                cnt += 1
                left += 1
                right -= 1
            elif cur < 0:
                left += 1
            else:
                right -= 1
    print(cnt)