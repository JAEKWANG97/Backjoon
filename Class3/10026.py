import sys

N = int(sys.stdin.readline())
lines = sys.stdin.readlines()

graph = []

for line in lines:
    graph.append(list(line.strip()))

def divide_section(graph, N):
    red = []
    green = []
    blue = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "R":
                red.append((i,j))
            if graph[i][j] == "G":
                green.append((i,j))
            if graph[i][j] == "B":
                blue.append((i,j))
    return red, green, blue
from collections import deque


red , green ,blue = divide_section(graph , N)
red_cnt,green_cnt,blue_cnt = 0, 0, 0
    
# color == R or G or B
def bfs(graph , N , color , color_index):
    visit = [[False for _ in range(N)] for _ in range(N)]
    que = deque()
    count = 0
    for i,j in color_index:
        if not visit[i][j]:
            que.append((i,j))
            visit[i][j] = True
            count += 1
            while que:
                cur = que.popleft()
                x,y = cur
                visit[x][y] = True
                
                dx = [1,-1,0,0]
                dy = [0,0,1,-1]
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visit[nx][ny] and graph[nx][ny] in color:
                            visit[nx][ny] = True
                            que.append((nx,ny))
    return count

color = ['R' , 'G' , 'B']
red_cnt = bfs(graph , N , color[0] , red)
green_cnt = bfs(graph , N , color[1] , green)
blue_cnt = bfs(graph , N , color[2] , blue)
red_green_cnt = bfs(graph , N , color[0:2] , red+green)

print(red_cnt+green_cnt+blue_cnt ,red_green_cnt + blue_cnt )