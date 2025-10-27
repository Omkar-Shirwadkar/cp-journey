t = int(input())
for _ in range(t):
    x, y = [int(x) for x in input().split()]
    a, b = [int(x) for x in input().split()]
    if a * 2 > b:
        mini = min(x, y)
        maxi = max(x, y)
        ans = mini * b
        ans += (maxi - mini) * a
    else:
        ans = (x + y) * a
    print(ans)