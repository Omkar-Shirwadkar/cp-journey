# no less than a in the front
# no more than b in the back
n, a, b = [int(x) for x in input().split()]
print(n - max(a + 1, n - b) + 1)