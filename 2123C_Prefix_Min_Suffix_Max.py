t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [0] * n
    suff = [0] * n
    pref[0] = arr[0]
    suff[n - 1] = arr[n - 1]
    for i in range(1, n):
        pref[i] = min(pref[i - 1],arr[i])
    for i in range(n - 2, -1, -1):
        suff[i] = max(suff[i + 1],arr[i])
    ans = ""
    for i in range(n):
        if arr[i] == pref[i] or arr[i] == suff[i]:
            ans += "1"
        else:
            ans += "0"
    print(ans)