t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    sm = bg = 0
    for i in range(n):
        if a[i] > b[i]:
            bg += a[i] - b[i]
        else:
            sm += b[i] - a[i]
    print(bg + 1)