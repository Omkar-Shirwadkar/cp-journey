def min_swaps(positions):
    k = len(positions)
    if k <= 1:
        return 0
    mid = k // 2
    median = positions[mid]
    cost = 0
    for i in range(k):
        cost += abs(positions[i] - (median - mid + i))
    return cost

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a_idx = []
    b_idx = []
    for i in range(n):
        if s[i] == "a":
            a_idx.append(i)
        else:
            b_idx.append(i)
    ans = min(min_swaps(a_idx), min_swaps(b_idx))
    print(ans)