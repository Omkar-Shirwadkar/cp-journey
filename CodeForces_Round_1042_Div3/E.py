t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    if arr[-1] != brr[-1]:
        print("NO")
        continue

    possible = True
    for i in range(n - 1):
        if arr[i] != brr[i]:
            temp = arr[i] ^ arr[i+1]
            if temp == brr[i]:
                arr[i] = brr[i]
    for i in range(n - 2, -1, -1):
        if arr[i] != brr[i]:
            temp = arr[i] ^ arr[i + 1]
            # print("Temp", temp)
            if temp != brr[i]:
                possible = False
                break
            else:
                arr[i] = brr[i]
    if possible:
        print("YES")
    else:
        print("NO")