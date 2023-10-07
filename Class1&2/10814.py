# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

import sys

n = int(sys.stdin.readline().strip())

join_list = []

for i in range(n):
    input = list(sys.stdin.readline().strip().split(' '))
    age = int(input[0])
    name = input[1]
    join_list.append([age,name,i])
    
join_list = sorted(join_list, key=lambda x: (x[0], x[2]))

for i in range(len(join_list)):
    print(join_list[i][0], join_list[i][1])