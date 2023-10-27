
import sys

T = int(input())

def dfs(arr , visit , m , n):
    directions = [(1,0) , (0,1) , (-1 , 0) , (0,-1)]
    stack =[]
    count = 0
    for i in range(m):
        for j in range(n):
            if visit[j][i] == False and arr[j][i] == 1:
                stack.append([j,i])
                count += 1
                while stack:
                    start_node = stack.pop()
                    y = start_node[0]
                    x = start_node[1]
                    visit[y][x] = True
                    for dx, dy in directions:
                        ny, nx = y + dy, x + dx 
                        
                        if arr[ny][nx] == 1 and visit[ny][nx] == False and ny < n and nx < m:
                            stack.append([ny,nx])
                            visit[ny][nx] = True
                  
            else:
                continue
    return count
for _ in range(T):
    m,n,k = map(int , sys.stdin.readline().strip().split(' '))
    count = 0
    arr = [[0 for j in range(m+1)] for i in range(n+1)]
    visit = [[False for j in range(m+1)]for i in range(n+1)]
    for i in range(0,k):
        x,y = map(int, sys.stdin.readline().strip().split(' '))
        arr[y][x] = 1
    print(dfs(arr,visit,m,n))