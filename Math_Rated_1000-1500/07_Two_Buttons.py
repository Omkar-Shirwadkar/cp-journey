n, m = [int(x) for x in input().split()]
ans = 0
while m > n:
    if m % 2:
        m += 1
    else:
        m = m // 2
    ans += 1
print(ans + (n - m))