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

T = int(input())

for _ in range(T):
    m,n,k = map(int , sys.stdin.readline().strip().split(' '))
    count = 0
    arr = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(0,k):
        x,y = map(int, sys.stdin.readline().strip().split(' '))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        arr[y][x] = 1
        value = True
        for dx, dy in directions:
            ny, nx = y + dy, x + dx 
            try:
                if arr[ny][nx] == 1:
                    value = False
                    break
            except IndexError:
                pass
        if value: count += 1

    print(count)
