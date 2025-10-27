# 0: 1 
# 1, 5, 9: 8 
# 2, 6: 4 
# 3, 7: 2 
# 4, 8: 6  
n = int(input())
map8power = {0: 6, 1: 8, 2: 4, 3: 2}
if n == 0:
    print(1)
else:
    print(map8power[n % 4])