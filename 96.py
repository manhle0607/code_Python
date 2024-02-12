n = int(input())
matrix = [[]] * n
for i in range(n):
    matrix[i] = [int(i) for i in input().split()]
sumUp, sumDown = 0, 0
for i in range(n):
    for j in range(n):
        if j > n-1-i:
            sumDown += matrix[i][j]
        elif j < n-1-i:
            sumUp += matrix[i][j]
k = int(input())
gttd = int(abs(sumUp - sumDown))
print("YES" if gttd <= k else "NO")
print(gttd)