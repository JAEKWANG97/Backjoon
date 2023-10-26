#                                                                                                                                                                                           '''
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트 케이스에 대해 
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
# '''

# T = int(input())

# M은 가로 길이
# N은 세로 길이
# K는 심어져있는 배추 위치의 개수
# 그 이하는 배추의 좌표
# 처음 방법이 틀렸어.
# 처음엔 입력하는 배추의 좌표를 그냥 좌우상하만 살피면 된다고 생각했다.
# 하지만 중간에 집합이 겹쳐서 2개였던 집합이 1개로 합쳐지는 경우가 있다!

import sys

    
def dfs(x, y, visited, arr):
    # 주어진 배추밭의 크기를 벗어나는 경우 종료
    if x < 0 or x >= len(arr[0]) or y < 0 or y >= len(arr):
        return False
    # 해당 위치에 배추가 없거나 이미 방문한 경우 종료
    if not arr[y][x] or visited[y][x]:
        return False
    # 현재 위치를 방문 처리
    visited[y][x] = True
    # 상, 하, 좌, 우 위치에 대해 DFS 수행
    dfs(x-1, y, visited, arr)
    dfs(x+1, y, visited, arr)
    dfs(x, y-1, visited, arr)
    dfs(x, y+1, visited, arr)
    return True


T = int(input())

for _ in range(T):
    m,n,k = map(int , sys.stdin.readline().strip().split(' '))
    count = 0
    arr = [[False for j in range(m)] for i in range(n)]
    xy = []
    for i in range(0,k):
        x,y = map(int, sys.stdin.readline().strip().split(' '))
        arr[y][x] = True
        xy.append((x,y))
    print(count_cabbage_groups(m, n, k, xy))




        
    
