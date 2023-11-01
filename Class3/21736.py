n,m = map(int , input().split())

arr = [list(input().split()) for _ in range(n)]

# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장

for i in range(n):
    arr[i] = list(arr[i][0])


def search_doyun(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                return (i,j)
    return

from collections import deque

def bfs(n,m,arr,node):
    que = deque()
    que.append(node)
    visit = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    while que:
        cur = que.popleft()
        i,j = cur
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        if arr[i][j] == 'P':
            count+=1
        for d in range(4):
            ni, nj = i + dx[d] , j + dy[d]
            if 0<=ni<n and 0<=nj<m:
                if not visit[ni][nj] and arr[ni][nj] in ["O" , "P"]:
                    que.append((ni,nj))
                    visit[ni][nj] = True
                       
            
            
            
        # for d in range(4):
        #     ni, nj = i + dx[d], j + dy[d]
        #     if 0 <= ni < n and 0 <= nj < m:
        #         if not visit[ni][nj] and arr[ni][nj] in ["O","P"] :
        #             que.append((ni, nj))
        #             visit[ni][nj] = True
                    
    return count
node = search_doyun(arr)
cnt = bfs(n,m,arr,node)
if cnt == 0:
    print("TT")
else:
    print(cnt)