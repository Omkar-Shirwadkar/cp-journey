t = int(input())
for _ in range(t):
    n, j, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    ourInteger = a[j - 1]
    isMax = (ourInteger == max(a))
    if k != 1 or isMax:
        print("Yes")
    else:
        print("No")