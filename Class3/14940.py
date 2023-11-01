n, m = map(int, input().strip().split())

arr = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def bfs(arr,node):
    visit = [[False for _ in range(m)] for _ in range(n)]
    new_arr = [[0 for _ in range(m)] for _ in range(n)]
    que = deque()
    que.append(node)
    visit[node[0]][node[1]] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_arr = [[-1 if arr[i][j] == 1 else arr[i][j] for j in range(m)] for i in range(n)]
    while que:
        cur = que.popleft()
        i,j,cnt = cur
        
        new_arr[i][j] = cnt
        
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            
            if 0 <= ni < n and 0 <= nj < m:
                if  not visit[ni][nj] and arr[ni][nj] in [1, 2]:
                    que.append((ni, nj, cnt+1))
                    visit[ni][nj] = True
    for i in range(n):
        for j in range(m):
            if visit[i][j] == False:
                new_arr[i][j] = -1
            if arr[i][j] == 0:
                new_arr[i][j] = 0
                
  
    return new_arr


def search_node(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return (i,j,0)
            
node = search_node(arr)

new_arr = bfs(arr,node)
for i in range(n):
    for j in range(m):
        print(new_arr[i][j] , end=' ')
    print()