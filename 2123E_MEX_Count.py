t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    excl = set(range(n + 1))
    
    for x in a:
        freq[x] = freq.get(x, 0) + 1
        excl.discard(x)
    
    invfreq = {}
    for key, value in freq.items():
        if value not in invfreq:
            invfreq[value] = []
        invfreq[value].append(key)
    
    mex = min(excl)
    vals = set()
    vals.add(mex)
    
    for k in range(n + 1):
        vals.discard(n - k + 1)
        for i in invfreq.get(k, []):
            if i <= min(mex, n - k):
                vals.add(i)
        print(len(vals), end=' ' if k != n else '\n')