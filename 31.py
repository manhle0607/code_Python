a,b,c = map(int, input().split())
bMin = (int(a/b) + 1) * b - a 
bMax = int(c/b) * b - a
if bMin <= bMax:
    for i in range(bMin, bMax + 1, b):
        
            print(i, end = " ")
else:
    print(-1)
    
        