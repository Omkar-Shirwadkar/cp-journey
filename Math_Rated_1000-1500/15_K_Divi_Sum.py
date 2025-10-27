# ceil of [n / k] == floor of [(n + k - 1) / k]
t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    cf = (n + k - 1) // k
    k *= cf
    print((k + n - 1) // n)          