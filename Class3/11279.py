import heapq
import sys
n = int(input())
heap = []

numbers = [int(line.strip()) for line in sys.stdin.readlines()]
for num in numbers:
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        num = heapq.heappush(heap, (-num,num))