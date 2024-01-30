for t in range(int(input())):
    s = input()
    s = s + 'z'
    tong = 0
    ans = -99*21
    for i in range(len(s)):
        if s[i].isalpha():
            if i != 1 and s[i-1].isdigit():
                ans = max(ans, tong)
                tong = 0
        else:
            tong = tong * 10 + int(s[i])
    print(ans)