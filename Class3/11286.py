import heapq

import sys

# 첫 줄에 입력받을 줄의 수를 지정합니다.
n = int(sys.stdin.readline())

# 이후의 줄들을 한 번에 입력받습니다.
lines = sys.stdin.readlines()

# 문자열 리스트를 정수 리스트로 변환합니다.
nums = [int(line.strip()) for line in lines]

heap = []

for x in nums:
    if x != 0:
        heapq.heappush(heap, (abs(x) , x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)