t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if k == 0:
        print(a.count(0))
    else:
        curr = a.count(k)
        seta = set()
        for i in a:
            if i < k:
                seta.add(i)
        required = k
        available = len(seta)
        print(max(curr, required - available))