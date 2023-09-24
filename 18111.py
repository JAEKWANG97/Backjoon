import sys


# n, m, b = map(int, sys.stdin.readline().split(" "))
n, m, b = 3, 4, 0


# 모든 data를 더하면 고 생각하면 됨
# 최소시간을 골라야 함
# 땅의 높이도 골라야함

# 제거히는데 2초
# 설치하는데 1초

# 상대적으로 설치만 하는게 빠름

# 최소한의 제거 + 최대한의 설치

# data = []
# for i in range(n):
#     data += list(map(int, sys.stdin.readline().split(" ")))

# 모든 data의 합을 구하고

data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


# min에서 max 까지 브루트포스

min_total_time = None
h = None

for i in range(min(data), max(data)):
    # 제거된 블록의 수
    terminated_block = 0

    # 설치된 블록의 수
    mounted_block = 0

    # 만약 모든 높이가 i로 맞춰진다면
    for x in data:
        # 만약 x가 i보다 작다면 블럭을 설치해야함. 블럭의 갯수는 입력받은 블럭의 수와 제거한 블록의 수의 합임
        # 우선 x가 i보다 작다면 필요한 블럭의 총 개수를 구함
        # 반대로 제거해야할 블록의 총 수를 구함

        # 설치된 블록의 수가 목표 높이 보다 큰 경우
        # 제거할 block의 수
        if x - i > 0:
            terminated_block += 1
        # 설치된 블록의 수가 목표 높이 보다 작은 경우
        # 설치할 block의 수
        if x - i < 0:
            mounted_block += 1

    # 설치할 블록의 수가
    # 제거된 블록의 수와 인벤에 있는 블록의 수보다 적은지 확인, 적으면 해당 목표 높이는 continue
    if terminated_block + b < mounted_block:
        continue
    # 설치할 블록의 수가
    # 제거된 블록의 수와 인벤에 있는 블록의 수보다 같거나 큰지 확인, True면 해당 높이 맞추는 시간 계산
    # 설치는 +1 제거는 +2
    else:
        total_time = 0
        total_time += terminated_block * 2
        total_time += mounted_block * 1

    # 최소 총 시간이 None 이면 초기값으로 설정 아니면 비교 후 min인 time을 최소시간으로 설정
    if min_total_time is None:
        min_total_time = total_time
        h = i
    elif min_total_time > total_time:
        min_total_time = total_time
        h = i


print(min_total_time, h)


# arr =
# for item in merge_sort(arr):
#     sys.stdout.write(str(item) + "\n")
