n, m = [int(x) for x in input().split()]
lower_bound = (n + 1) // 2
ans = ((lower_bound + m - 1) // m ) * m
if ans > n:
    print(-1)
else:
    print(ans)