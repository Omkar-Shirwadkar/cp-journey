import math
m, n, a = [int(x) for x in input().split()]
s1 = math.ceil(m / a)
s2 = math.ceil(n / a)
print(s1 * s2)