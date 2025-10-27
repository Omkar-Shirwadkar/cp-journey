t = int(input())
for _ in range(t):
    degree = int(input())
    exist = (360 % (180 - degree) == 0)
    if exist:
        print("YES")
    else:
        print("NO")