import sys

n = int(sys.stdin.readline().strip())

'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

'''
arr=[]
mid = 0

for i in range(n):
    num = int(sys.stdin.readline().strip())
    arr.append(num)

arr.sort()

def customRound(n):
    if n - int(n) >= 0.5:
        n = int(n) + 1
    else:
        n = int(n)
    return n

arr_dict = dict()

for x in arr:
    if x not in arr_dict:
        arr_dict[x] = 0
    arr_dict[x] += 1

def average(arr):
    return round(sum(arr)/len(arr))

def mode(arr_dict):
    max_val = max(arr_dict.values())
    mode_num = [k for k, v in arr_dict.items() if v == max_val]
    mode_num.sort()
    if len(mode_num) > 1:
        return mode_num[1]
    return mode_num[0]

def minMax(arr):
    return arr[-1] - arr[0]

def median(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[len(arr)//2]

print(average(arr))
print(median(arr))
print(mode(arr_dict))
print(minMax(arr))