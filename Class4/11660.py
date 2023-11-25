import sys

n, m = map(int, sys.stdin.readline().split())

# 입력 행렬을 읽음
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2차원 누적 합 배열 초기화
def initialize_2d_cumulative_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix_sum_arr = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum_arr[i][j] = prefix_sum_arr[i - 1][j] + prefix_sum_arr[i][j - 1] - prefix_sum_arr[i - 1][j - 1] + matrix[i - 1][j - 1]
    return prefix_sum_arr

cumulative_sum = initialize_2d_cumulative_sum(arr)

# 누적 합을 이용해 쿼리 처리
def query_cumulative_sum(cum_sum, x1, y1, x2, y2):
    return cum_sum[x2][y2] - cum_sum[x1 - 1][y2] - cum_sum[x2][y1 - 1] + cum_sum[x1 - 1][y1 - 1]

# 각 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(query_cumulative_sum(cumulative_sum, x1, y1, x2, y2))
