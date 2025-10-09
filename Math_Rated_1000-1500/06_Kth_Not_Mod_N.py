t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    # To get the kth positive number divided by n
    # If we do k divided by n resulting in quotient a1
    # then we shift the integer to the right by a1
    # now we will have to remove the divisors from the a1 which are shifted
    # this keeps on going till r times until we find an ar which is less than n
    # this merely sums up to (k - 1) / (n - 1)
    needed = (k - 1) // (n - 1)
    print(k + needed)