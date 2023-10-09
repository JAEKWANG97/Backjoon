# 분해합

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

import sys

# 입력받은 N
n = int(sys.stdin.readline().strip())


# 분해합이란 예를 들어 n이 256이라면 => 245 + 2 + 4 + 5 가 될 수 있다.
# 그 수와 각 자릿수의 합이 256을 만들면 그 수는 생성자가 된다.
# 생성자는 많을 수 있고 없을 수 있다.
# 가장 작은 생성자를 출력하라

# DP 문제 비슷한거같은데

1
# 일의 자리 숫자는 생성자가 없음
# 10 => 10 + 1 !== 10 10도 그러함 하지만 5가 있음.
arr = []

gen_dict = dict()

for i in range(1,n+1):
    temp = i
    nums = int(str(temp)[-1])
    while True:
        int_temp = int(temp)
        str_temp = str(temp)
        if len(str(temp)) > 1:
            temp = str_temp[:len(str_temp)-1]
            nums += int(temp) % 10
        else:
            break
    # print(nums)
    generator = i + nums
    
    if generator not in gen_dict:
        gen_dict[generator] = i
    
if n in gen_dict:
    print(gen_dict[n])
else:
    print(0)
    
    

'''
10 + 1 + 0 = 11
11 + 1 + 1 = 13
12 + 1 + 2 = 15
13 + 1 + 3 = 17
14 + 1 + 4 = 19
.
.
.
.
.
20 + 2 + 2 = 24
.
.
.
.
.
200 + 2 + 0 + 0 = 202
201 + 2 + 0 + 1 = 204
'''