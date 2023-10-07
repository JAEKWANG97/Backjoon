import sys

m = 1234567891
r = 31

# h = len(str)의 합 (i번 째 a * r의 i승 % m)
n = sys.stdin.readline()
str = sys.stdin.readline().strip()
h = 0
current_r = 1 
for x in str:
    h += (ord(x)-96) * current_r 
    current_r *= r
    
h %= m
print(h)