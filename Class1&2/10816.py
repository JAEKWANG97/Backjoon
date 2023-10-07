# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

# 3 0 0 1 2 0 0 2

import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int,list(sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline().strip())
m_list = list(map(int,list(sys.stdin.readline().strip().split())))

n_dict = dict()

for x in (n_list):
    if x not in n_dict:
        n_dict[x] = 0
    n_dict[x] += 1

answer = []

for x in m_list:
    if x in n_dict:
        print(n_dict[x] , end=" ")
    else:
        print(0 , end=" ")