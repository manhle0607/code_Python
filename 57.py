for t in range(int(input())):
    tong = str(sum(int(i) for i in input()))
    print('YES' if len(tong) > 1 and tong == tong[::-1] else 'NO')