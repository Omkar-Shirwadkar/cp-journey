a = int(input())
b = int(input())
c = int(input())
if a == 1 and c == 1:
    print(a + b + c)
elif a == 1:
    print((a + b) * c)
elif c == 1:
    print(a * (b + c))
elif b == 1:
    print(max((a + 1) * c, (c + 1) * a))
else:
    print(a * b * c)