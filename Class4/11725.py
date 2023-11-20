import sys
from collections import defaultdict

n = int(sys.stdin.readline())

lines = sys.stdin.readlines()

tree = defaultdict(list)

for line in lines:
    a, b = map(int, line.split())
    tree[a].append(b)
    tree[b].append(a)

stack = []
visit = [False for _ in range(n + 1)]
ans_dict = defaultdict(int)

stack.append(1)
visit[1] = True
while stack:
    cur = stack.pop()
    for x in tree[cur]:
        if not visit[x]:
            stack.append(x)
            ans_dict[x] = cur
            visit[x] = True
for key, value in sorted(ans_dict.items()):
    print(value)
