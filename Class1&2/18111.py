import sys


n, m, b = map(int, sys.stdin.readline().split())
# # n, m, b = 1,3,4



data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# data = [5,3,3]
# n, m, b = 2, 2, 35
# data = [20,10,190,40]


max_block = max(data)
min_block = min(data)



min_total_time = sys.maxsize
h = 0

for i in range(min_block, max_block + 1):
    terminated_block , mounted_block = 0 , 0
    
    for x in range(n):
        for y in range(m):
            if data[x][y] > i :
                terminated_block += data[x][y]- i
            else:
                mounted_block += i - data[x][y] 

    if terminated_block + b >= mounted_block:
        total_time = terminated_block * 2 + mounted_block
        if total_time < min_total_time:
            min_total_time = total_time
            h = i
        

        
        

print(min_total_time, h)
