t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(n):
        if i & 1:
            ans.append(3)
        else:
            ans.append(-1)
    if n & 1 == 0:
        ans[-1] = 2
    print(*ans)