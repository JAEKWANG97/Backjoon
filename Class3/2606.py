'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

#  개념만 보고 처음 구현해본 그래프?
import sys
from collections import deque

n =int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
computer_dict = dict()

for i in range(m):
    a,b = map(int, sys.stdin.readline().strip().split(' '))
    if a not in computer_dict:
        computer_dict[a] = []
    if b not in computer_dict:
        computer_dict[b] = []
    computer_dict[a].append(b)
    computer_dict[b].append(a)


seek = []
queue = deque()
visited = [False] * (n+1)
if 1 in computer_dict:
    queue.extendleft(computer_dict[1])
count = 0
while len(queue)>0:
    tmp =queue.popleft()
    if not visited[tmp] and tmp != 1:
        seek.append(tmp)
        visited[tmp] = True
        count += 1
        if tmp in computer_dict:
            for x in  computer_dict[tmp]:
                if not visited[x]:                
                    queue.append(x)
    else:
        continue

print(count)