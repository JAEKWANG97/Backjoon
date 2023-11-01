from collections import deque

n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

def bfs(arr):
    que = deque()
    node = (0,0,1)
    visit = [[False for _ in range(m)] for _ in range(n)]
    
    
    que.append(node)
    i,j,cnt = node
    visit[i][j] = True
    while que:
        cur = que.popleft()
        i , j , cnt = cur
        if i == n- 1 and j == m- 1:
            return cnt
        dx = [1,-1,0,0]
        dy = [0, 0,1,-1]
        for d in range(4):
            nx = dx[d]+i 
            ny = dy[d]+j
            if 0<=nx<n and 0<=ny<m:
                if not visit[nx][ny] and arr[nx][ny] == '1':
                    que.append((nx,ny,cnt+1))
                    visit[nx][ny] = True

print(bfs(arr))