import sys

n = int(input())
arr = []
lines = sys.stdin.readlines()
dp = [[0] * 3 for _ in range(n)]

for line in lines:
    