import sys

# 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

from collections import defaultdict

tree_dict = defaultdict(int)
min_tree = 0
max_tree = max(arr)

for x in arr:
    tree_dict[x] += 1

result = 0
# 이분 탐색
while min_tree <= max_tree:
    height = (max_tree + min_tree) // 2
    sum = 0
    for key, value in tree_dict.items():
        if key > height:
            sum += (key - height) * value

    if sum >= m:
        result = height
        min_tree = height + 1
    else:
        max_tree = height - 1

print(result)
