'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1.5 초	4 MB (하단 참고)	91499	27445	20076	29.175%
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
'''

n = int(input())
import sys
arr = set()
for i in range(n):
    cmd = list(sys.stdin.readline().strip().split(' '))
    if len(cmd) > 1:
        value = int(cmd[1])
    cmd = cmd[0]
    if cmd == 'add': 
        arr.add(value)
    elif cmd == 'remove' : 
        arr.discard(value)

    elif cmd == 'check' : 
        if value in arr:
            # print(arr , value , value in arr)
            print(1)
        else:
            # print(arr,value , value in arr)
            print(0)
            
    elif cmd == 'toggle' :
        if value in arr:
            
            arr.discard(value)
            # print(arr , value)
        else:
            arr.add(value)
            # print(arr , value)
    elif cmd == 'all' : 
        arr.clear()
        arr.update(range(1, 21))
    elif cmd == 'empty' :
        arr.clear()