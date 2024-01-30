for t in range(int(input())):
    s = input()
    s = s + 'z'
    tong = 0
    ans = 10**20
    for i in range(len(s)):
        if s[i].isalpha():
            if i != 0 and s[i-1].isdigit():
                ans = min(ans, tong)
                tong = 0
        else:
            tong = tong * 10 + int(s[i])
    print(ans)
                
