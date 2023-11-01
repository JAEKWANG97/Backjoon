# 케빈!
import sys
from collections import defaultdict
n,m = map(int , sys.stdin.readline().strip().split())

graph = defaultdict(set)
for _ in range(m):
    i,j = map(int , sys.stdin.readline().strip().split())
    graph[i].add(j)
    graph[j].add(i)
    



from collections import deque

def bfs(graph , node):
    que = deque()
    visit = [False for _ in range(n+1)]
    que.append(node)
    visit[node[0]] = True
    count = 0
    while que:
        cur = que.popleft()
        num , cnt = cur
        count += cnt
        for x in graph[num]:
            if not visit[x]:
                que.append((x , cnt + 1))
                visit[x] = True
    return count
min_value = float("inf")
min_key = float("inf")
        
# print(bfs(graph , (2,0)))

for key in graph.keys():
    value = bfs(graph , (key,0))
    if value < min_value:
        min_key = key
        min_value = value
    elif value == min_value:
        if min_key > key:
            min_key = key
print(min_key)
