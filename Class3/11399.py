# 1~n 까지의 사람
# 그리고 p1 ~ pn 까지 순서대로 n번이 인출하는시간
# 가장 p1~pn을 오름차순으로 정렬하는 문제
# 누적합 구하는 문제
import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().strip().split(' ')))

sum_arr = []

arr.sort()

sum_time = 0

for time in arr:
    sum_time += time
    sum_arr.append(sum_time)
    
print(sum(sum_arr))