import sys
sum = 0
for x in list(map(int , list(sys.stdin.readline().strip().split(' ')))):
    sum += x**2

print(sum % 10)