# 듣도 못한 사람의 수 N
# 보도 못한 사람의 수 M
'''
첫째 줄에 듣도 못한 사람의 수 N
보도 못한 사람의 수 M이 주어진다.

이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.

이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다.

N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

듣보잡의 수와 그 명단을 사전순으로 출력한다.

입력
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

'''

# 사전 순으로 출력해야함.

import sys

n , m = map(int , sys.stdin.readline().strip().split(' '))

name_dict = dict()
for i in range(n+m):
    name  = sys.stdin.readline().strip()
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] += 1

name_list = []
count =0 
for key , value in name_dict.items():
    if value > 1:
        count += 1
        name_list.append(key)
        
name_list.sort()
print(count)
for name in name_list:
    print(name)