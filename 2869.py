# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)


import sys

str = list(sys.stdin.readline().split(' '))
a = int(str[0])
b = int(str[1])
v = int(str[2])

days = v // (a - b)

v_temp = v - a #v_temp 까지는 최소한 자면서 올라와야함. 
days = v_temp // (a-b) +1 # 때문에 days는 자면서 올라오는 기간
left_v = v_temp % (a-b)
# 남은 높이가 0보다 큰지 아닌지 판단.  
if left_v  > 0:
     print( days +  1 )
else:
    print( days )
