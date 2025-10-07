t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    seen = [False] * (k+1)
    curr = a.count(k)
    available = 0
    for x in a:
        if x < k and not seen[x]:
            seen[x] = True
            available += 1
    print(max(curr, k - available))