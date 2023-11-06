# 우선순위 큐
import sys
from collections import defaultdict
import heapq

# Main logic
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    max_heap = []
    min_heap = []
    heap_dict = defaultdict(int)
    for _ in range(n):
        cmd, *args = sys.stdin.readline().strip().split()
        num = int(args[0])
        if cmd == "I":
            heapq.heappush(max_heap , -num)
            heapq.heappush(min_heap , num)
            heap_dict[num] += 1
        else:
            if min_heap and max_heap:
                if cmd == 'D' and num == 1:
                    while max_heap:
                        max_value = -1 *  heapq.heappop(max_heap)
                        if heap_dict[max_value] > 0:
                            heap_dict[max_value] -= 1
                            break
                elif cmd == 'D' and num == -1:
                        while min_heap:
                            min_value = heapq.heappop(min_heap)
                            if heap_dict[min_value] > 0:
                                heap_dict[min_value] -= 1
                                break
    while min_heap and heap_dict[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    while max_heap and heap_dict[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
        
    
    
    if not max_heap or not min_heap:
        print("EMPTY")

    while max_heap:
        max_value = -1 * heapq.heappop(max_heap)
        if heap_dict[max_value] > 0:
            print(max_value , end=" ")
            break
    while min_heap:
        min_value = heapq.heappop(min_heap)
        if heap_dict[min_value] > 0 :
            print(min_value)
            break
        
    
    