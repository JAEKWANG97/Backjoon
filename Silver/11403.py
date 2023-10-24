from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# i , j 까지 가는 경로

visit = [[0 for _ in range(n+1)] for _ in range(n+1)]

new_arr = [[] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1, n+1):
        if arr[i-1][j-1] == 1:
            new_arr[i].append(j)
            
queue = deque([i for i in range(len(new_arr))])
        
start_node = [i for i in range(1,n+1)]

def dfs(visit , start_node, new_arr):
        for num in start_node:
            # startNode 선정
            # visit에 true로 변경
            # i to j
            # 여기서부터 dfs임
            stack = []
            stack.extend(new_arr[num])
            while (stack):
                current_node = stack.pop()
                if visit[num][current_node] == 0:
                    visit[num][current_node] = 1
                    # 찾은 다음에는 stack에 넣어 줘야함 
                    # stack에는 없는 번호로다가 
                    # 그리고 visit이 False인 번호로다가
                    for x in new_arr[current_node]:
                        if x not in stack and visit[num][x] == 0:
                            stack.append(x)
        return visit

answer = dfs(visit , start_node , new_arr)

for i in range(1, n+1):
    for j in range(1,n+1):
        print(answer[i][j] , end=" ")
    print()
# 방향 그래프 G