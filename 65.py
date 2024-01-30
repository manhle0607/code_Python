for t in range(int(input())):
    s = input()
    tich = 0
    tong = 0
    for i in range(len(s)):
        if i % 2 == 0:
            tong += int(s[i])
        else:
            if int(s[i]) != 0:
                if tich == 0:
                    tich = int(s[i])
                else:
                    tich *= int(s[i])
                    
    print(str(tong) + " " + str(tich)) 