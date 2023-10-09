import sys

n = int(sys.stdin.readline().strip())

# 각 항목을 (y, x) 형태의 튜플로 저장
arr = [(y, x) for x, y in [map(int, sys.stdin.readline().strip().split(' ')) for _ in range(n)]]
arr.sort()

for y, x in arr:
    print(x, y)
    
    
'''
###########################################
###########################################
###########################################
###########################################
'''



