import heapq
import sys

n = int(sys.stdin.readline().strip())
sorted_numbers = []
heapq.heapify(sorted_numbers)
for i in range(0,n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(sorted_numbers) > 0:
            print(heapq.heappop(sorted_numbers))
        else:
            print(0)
    else:
        heapq.heappush(sorted_numbers, num)