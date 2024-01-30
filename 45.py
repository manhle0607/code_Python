for t in range(int(input())):
    s = int(input())
    sum = 0
    for i in range(2-s%2, s+1, 2):
        sum += 1/i
    print('{:.6f}'.format(sum))