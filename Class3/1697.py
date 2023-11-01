import sys

n , k = map(int , sys.stdin.readline().strip().split())

from collections import deque

queue = deque()

queue.append((n,0))

visit = [False for _ in range(100001)]
visit[n] = True
while queue:
    cur_n , cur_cnt = map(int , queue.popleft())
    if cur_n == k: 
        print(cur_cnt)
        break
    
    next = cur_n  + 1
    if(next >= 0 and next <= 100000 and visit[next] == False):
        visit[next] = True
        queue.append((next, cur_cnt+1))
        
    next = cur_n  - 1
    if(next >= 0 and next <= 100000 and visit[next] == False):
        visit[next] = True
        queue.append((next, cur_cnt+1))
        
    next = cur_n  * 2
    if(next >= 0 and next <= 100000 and visit[next] == False):
        visit[next] = True
        queue.append((next, cur_cnt+1))
        
    