n, l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
maxD = a[0]
for i in range(n - 1):
    maxD = max(maxD, (a[i + 1] - a[i]) / 2)

maxD = max(maxD, l - a[-1])
print(maxD)