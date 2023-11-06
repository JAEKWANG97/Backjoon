from collections import deque
import sys

T = int(sys.stdin.readline().strip())


def cal_d(n):
    return (2 * n) % 10000

def cal_s(n):
    return 9999 if n == 0 else n - 1

def cal_l(n):
    
    return (n%1000) * 10 + (n // 1000)

def cal_r(n):

    return (n%10) * 1000 + n % 1000

def bfs(start, target):
    visit = [False for _ in range(10000)]
    que = deque()
    que.append((start, ""))
    visit[start] = True
    
    while que:
        cur, cmd = que.popleft()
        if cur == target:
            return cmd

        # D
        next_d = cal_d(cur)
        if not visit[next_d]:
            visit[next_d] = True
            que.append((next_d, cmd + "D"))

        # S
        next_s = cal_s(cur)
        if not visit[next_s]:
            visit[next_s] = True
            que.append((next_s, cmd + "S"))

        # L
        next_l = cal_l(cur)
        if not visit[next_l]:
            visit[next_l] = True
            que.append((next_l, cmd + "L"))

        # R
        next_r = cal_r(cur)
        if not visit[next_r]:
            visit[next_r] = True
            que.append((next_r, cmd + "R"))

for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    cmd = bfs(n, m)
    print(cmd)
