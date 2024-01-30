for t in range(int(input())):
    s = int(input())
    a = [int(i) for i in input().split()]
    if len(a) == 1:
        print(a[0])
    else:
        m, cnt, ans = {}, 1, a[0]
        for i in a:
            if i in m:
                m[i] += 1
                if m[i] > 1:
                    cnt, ans = m[i], i
            else:
                m[i] = 1
        if cnt * 2 > len(a):
            print(ans)
        else:
            print("NO")