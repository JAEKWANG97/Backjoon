import sys
from collections import deque, defaultdict

N, M, X = map(int, input().split())
graph = defaultdict(list)
reverse_graph = defaultdict(list)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

def bfs(graph, start):
    que = deque([start])
    visit = [False] * (N + 1)
    visit[start] = True
    count = 0
    while que:
        cur = que.popleft()
        for item in graph[cur]:
            if not visit[item]:
                que.append(item)
                visit[item] = True
                count += 1
    return count

won_count = bfs(graph, X)
lost_count = bfs(reverse_graph, X)

highest_rank = 1 + lost_count
lowest_rank = N - won_count

print(highest_rank, lowest_rank)
