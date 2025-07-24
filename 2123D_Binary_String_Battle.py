t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    s = input()
    ones = s.count("1")
    if ones <= k or n < 2 * k:
        print("Alice")
    else:
        print("Bob")