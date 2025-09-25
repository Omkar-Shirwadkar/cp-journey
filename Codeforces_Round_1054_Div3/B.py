t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    maxD = 0
    for i in range(0, n, 2):
        maxD = max(maxD, a[i + 1] - a[i])
    print(maxD)