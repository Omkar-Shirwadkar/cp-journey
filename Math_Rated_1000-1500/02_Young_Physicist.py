n = int(input())
a = [0, 0, 0]
for _ in range(n):
    temp = [int(s) for s in input().split()]
    a[0] += temp[0]
    a[1] += temp[1]
    a[2] += temp[2]
if a == [0, 0, 0]:
    print("YES")
else:
    print("NO")