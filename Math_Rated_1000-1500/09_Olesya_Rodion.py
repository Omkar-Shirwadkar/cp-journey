n, t = [int(x) for x in input().split()]
if n == 1 and t == 10:
    print(-1)
else:
    remainder = (10 ** (n - 1)) % t
    print((10 ** (n - 1)) + (t - remainder))