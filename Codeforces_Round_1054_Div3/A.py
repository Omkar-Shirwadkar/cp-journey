t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    zeros = a.count(0)
    ans = zeros
    nega = 0
    for b in a:
        if b < 0:
            nega += 1
    if nega % 2:
        ans += 2
    print(ans)