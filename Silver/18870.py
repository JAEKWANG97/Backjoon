# 정렬문제임
# 모든 수를 입력 받고 번호를 매기는것과 같음
# 근데 중복된 수는 같은 인덱스임
# sort와 딕셔너리를 사용할 계획

from collections import defaultdict
import sys
n = int(input())
arr = list(map(int, input().split()))

arr_dict = defaultdict(int)
sorted_arr = sorted(arr)
count = 0
for x in sorted_arr:
    if x not in arr_dict:
        arr_dict[x] = count
        count+=1
for x in arr:
    if x in arr_dict:
        print(arr_dict[x] , end=" ")