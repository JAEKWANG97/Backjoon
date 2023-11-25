import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph):
    que = deque([1])
    visit = [False] * (n + 1)
    visit[1] = True
    answer = [-1] * n
    distance = 0

    while que:
        for _ in range(len(que)):
            cur = que.popleft()
            answer[cur - 1] = distance
            for x in graph[cur]:
                if not visit[x]:
                    visit[x] = True
                    que.append(x)
        distance += 1

    return answer

q = int(sys.stdin.readline())
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    answer = bfs(graph)
    print(' '.join(map(str, answer)))
