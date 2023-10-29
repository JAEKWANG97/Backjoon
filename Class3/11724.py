from collections import defaultdict
import sys
n, m = map(int, input().strip().split())

graph = defaultdict(list)

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True
    
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
