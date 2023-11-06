import sys

n, m = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(visit, graph, x, y, path_sum, count, max_sum):
    if count == 4:
        return max(max_sum, path_sum)
    
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = True
            max_sum = dfs(visit, graph, nx, ny, path_sum + graph[nx][ny], count + 1, max_sum)
            visit[nx][ny] = False
    return max_sum

def check_exception_shapes(x, y, max_sum):
    # 각 테트로미노 모양에 대한 (dx, dy)의 조합
    shapes = [
        ([1, -1, 0], [0, 0, 1]),  # ㅗ 모양
        ([0, 1, -1], [-1, 0, 0]), # ㅜ 모양
        ([0, 1, 0], [-1, 0, 1]),  # ㅏ 모양
        ([0, -1, 0], [-1, 0, 1])  # ㅓ 모양
    ]
    for dxs,dys  in shapes:
        possible_sum = graph[x][y]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                possible_sum += graph[nx][ny]
            else:
                break
        max_sum = max(max_sum, possible_sum)
    return max_sum

visit = [[False for _ in range(m)] for _ in range(n)]

max_sum = 0
for i in range(n):
    for j in range(m):
        visit[i][j] = True
        max_sum = max(dfs(visit, graph, i, j, graph[i][j], 1, max_sum),check_exception_shapes(i, j, max_sum))
        visit[i][j] = False
print(max_sum)
