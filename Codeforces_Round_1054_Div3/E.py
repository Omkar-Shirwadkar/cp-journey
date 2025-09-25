from collections import defaultdict
def count_max(arr, X, l, r):
    n = len(arr)
    freq = defaultdict(int)
    cnt = 0
    left = 0
    res = 0
    
    for right in range(n):
        if freq[arr[right]] == 0:
            cnt += 1
        freq[arr[right]] += 1
        while cnt > X:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                cnt -= 1
            left += 1
        maxLeft = right - l + 1
        minLeft = max(left, right - r + 1)
        if maxLeft >= minLeft:
            res += maxLeft - minLeft + 1
    return res
t = int(input())
for _ in range(t):
    n, k, l, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    ans = count_max(a, k, l, r) - count_max(a, k-1, l, r)
    print(ans)