import sys
from collections import defaultdict
from collections import deque
n, m = map(int, sys.stdin.readline().split())

lines = sys.stdin.readlines()

ladders=defaultdict(int)
snakes=defaultdict(int)

i=0
for line in lines:
    if i < n:
        key,value = map(int,line.strip().split())
        ladders[key] = value
    if i >= n :
        key,value = map(int, line.strip().split())
        snakes[key] = value
    i+=1
    


def bfs(ladders, snakes):
    visit = [False for i in range(0,101)]
    que = deque()
    que.append((1,0))
    while que:
        cur , count = que.popleft()
        if cur in ladders:
            cur = ladders[cur]
        elif cur in snakes:
            cur = snakes[cur]                
            
        if cur == 100:
            print(count)
        
        for step in range(1,7):
            next = cur+step
            if 1<=next<=100:
                if not visit[next]:        
                    que.append((next,count+1))
                    visit[next] = True
                    
    
bfs(ladders, snakes)