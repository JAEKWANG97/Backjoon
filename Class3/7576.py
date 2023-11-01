m,n = map(int , input().strip().split())

arr = [list(map(int, input().split())) for _ in range(n)]
search_arr = []
def search_node(arr):
    node = []
    value = True
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                node.append((i,j,0))
            if arr[i][j] == 0:
                search_arr.append((i,j))
            if arr[i][j] == 0:
                value = False
    return node , value ,search_arr


from collections import deque

def bfs(arr, start_node , search_arr):
    ripe_time = [[float("inf") for _ in range (m)] for _ in range(n)]
    visit = [[True for _ in range(m)] for _ in range(n)]
    max_time = 0
    queue = deque(start_node)

    for i, j, cnt in start_node:
        ripe_time[i][j] = cnt
        visit[i][j] = True
        
    for i , j in search_arr:
        visit[i][j] = False

    while queue:
        node = queue.popleft()
        i , j , cnt = node
        ripe_time[i][j]= min(ripe_time[i][j] , cnt)
        max_time = max(ripe_time[i][j] , max_time)
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < n and 0 <= nj < m:
                if not visit[ni][nj] and arr[ni][nj] == 0 :
                    queue.append((ni, nj, cnt+1))
                    visit[ni][nj] = True
                elif not visit[ni][nj]:
                    visit[ni][nj] = True
    if  not all(all(row) for row in visit):
        return -1
    return max_time
    
        
start_node , value , search_arr = search_node(arr)
if value == True:
    print(0)
else:
    ripe_time = bfs(arr,start_node , search_arr)
    print(ripe_time)