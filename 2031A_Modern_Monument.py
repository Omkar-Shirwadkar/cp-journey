t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    nary = {}
    for i in arr:
        nary[i] = nary.get(i, 0) + 1
    maxCount = max(nary.values())
    print(n - maxCount)