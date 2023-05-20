import sys

str = sys.stdin.readline().rstrip().split(' ')
result = 0
for i in str:
    result += int(i)

print(result)