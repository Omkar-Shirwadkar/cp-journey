t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    lowerM = m * m
    if n >= lowerM and (n & 1 == m & 1):
        print("YES")
    else:
        print("NO")