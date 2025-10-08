import math
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


n = int(input())
arr = [int(x) for x in input().split()]
limit = 10 ** 6
primes = sieve(limit)


for num in arr:
    root = math.isqrt(num)
    if root * root == num and primes[root]:
        print("YES")
    else:
        print("NO")