from collections import Counter
t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    
    rem_cnnt = Counter(x % k for x in T)

    for s in S:
        r1 = s % k
        r_match1 = r1
        r_match2 = (-r1) % k

        if rem_cnnt[r_match1] > 0:
            rem_cnnt[r_match1] -= 1
        elif rem_cnnt[r_match2] > 0:
            rem_cnnt[r_match2] -= 1
        else:
            print("NO")
            break
    else:
        print("YES")