t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    nary = {}
    for i in range(n):
        diff = a[i] - i
        if diff in nary:
            nary[diff] += 1
        else:
            nary[diff] = 1
    vals = list(nary.values())
    ans = 0
    for i in vals:
        ans += ((i - 1) * i) // 2
    print(ans)