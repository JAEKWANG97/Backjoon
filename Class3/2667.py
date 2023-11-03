from collections import deque

n = int(input())

graph = [list(input().strip()) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
count_list = []
def bfs(graph,visit,i,j,count_list):
    que = deque()
    que.append((i,j))
    count = 0 
    visit[i][j] =  True
    while que:
        x,y = que.popleft()
        count += 1
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for d in range(4):
            nx , ny = dx[d] + x , dy[d] + y
            if 0<= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and graph[nx][ny] == "1":
                    que.append((nx,ny))
                visit[nx][ny] = True
    count_list.append(count)
    return visit,count_list

for i in range(n):
    for j in range(n):
        if not visit[i][j] and graph[i][j] == "1":
            visit , count_list = bfs(graph,visit,i,j,count_list)
print(len(count_list))            
for i in range(len(count_list)):
    print(count_list[i])